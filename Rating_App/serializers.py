from rest_framework import serializers
from Rating_App.models import MovieUserRatingModel

class MovieUserRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieUserRatingModel
        fields = '__all__'
