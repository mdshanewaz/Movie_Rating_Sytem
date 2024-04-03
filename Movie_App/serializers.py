from rest_framework import serializers
from Movie_App.models import MovieModel

class MovieSerializer(serializers.ModelSerializer):
    genre= serializers.CharField(source='genre.type', read_only=True)
    rating = serializers.CharField(source='rating.rating', read_only=True)

    class Meta:
        model = MovieModel
        fields = '__all__'


class MovieAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = '__all__'