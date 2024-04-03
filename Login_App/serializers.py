from rest_framework import serializers
from django.contrib.auth import authenticate
from Login_App.models import ProfileModel, CustomUesr

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        data['user'] = user
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='email.email', read_only=True)
    password = serializers.CharField(source='email.password', read_only=True)
    class Meta:
        model = ProfileModel
<<<<<<< HEAD
        exclude = ['date_joined', 'username']
=======
        exclude = ['date_joined', 'username']
>>>>>>> 8f02dedd8812efaa36fda5b0bde2468bf5d1d44b
