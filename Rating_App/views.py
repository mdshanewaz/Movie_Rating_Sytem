from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from Rating_App.models import MovieUserRatingModel
from Rating_App.serializers import MovieUserRatingSerializer

# Create your views here.

class MovieUserRatingListAPIView(generics.ListCreateAPIView):
    permission_class = [IsAuthenticated]

    queryset = MovieUserRatingModel.objects.all()
    serializer_class = MovieUserRatingSerializer


class MovieUserRatingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_class = [IsAuthenticated]    

    queryset = MovieUserRatingModel.objects.all()
    serializer_class = MovieUserRatingSerializer
