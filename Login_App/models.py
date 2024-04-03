from django.db import models

# Create custome user model and admin panel
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _ 

# To automatically create one to one objects
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class MyUserManager(BaseUserManager):

    """ A custom Manger to deal with phone number and email as unique identifer """
    def _create_user(self, email, password, **extra_fields):

        """ Create and save a user with given email, phone and password """
        if not email:
            raise ValueError("Email Must be set!")
        
        # Normalize email and phone number
        email = self.normalize_email(email)
        
        # Check if the email or phone number already exists
        if self.model.objects.filter(email=email).exists():
            raise ValueError("Email is already taken!")

        # Create and save the user
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser =True")
        return self._create_user(email, password, **extra_fields)


class CustomUesr(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)

    is_staff = models.BooleanField(
        _('staff status'),
        default = False,
        help_text = _('Designates whether the user can log in this site')
    )

    is_active = models.BooleanField(
        _('active'),
        default = True,
        help_text = _('Designate whether this user should be treated as active. Unselect this instead of deleting accounts')
    )

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

class ProfileModel(models.Model):
    email = models.OneToOneField(CustomUesr, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=264, blank=True)
    name = models.CharField(max_length=264, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username + "'s Profile"
    
    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        return True


@receiver(post_save, sender=CustomUesr)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)
        
    
@receiver(post_save, sender=CustomUesr)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()