from django.db import models

# Create your models here.

class GenreModel(models.Model):
    type = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.type


class RateModel(models.Model):
    rating = models.CharField(max_length=10, null=True)

    def __str__(self):
        if self.rating:
            return self.rating
        else:
            return "Unnamed"


class MovieModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    genre = models.ForeignKey(GenreModel, on_delete=models.CASCADE, null=True)
    rating = models.ForeignKey(RateModel, on_delete=models.CASCADE, null=True)
    release_date = models.DateField(null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Unnamed Movie"
    