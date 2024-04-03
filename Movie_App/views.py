from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from Movie_App.models import MovieModel
from Movie_App.serializers import MovieSerializer, MovieAddSerializer

# Create your views here.

class MovieListAPIView(generics.ListAPIView):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer

class MovieAddAPIView(generics.ListCreateAPIView):
    permission_class = [IsAuthenticated]

    queryset = MovieModel.objects.all()
    serializer_class = MovieAddSerializer

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_class = [IsAuthenticated]    

    queryset = MovieModel.objects.all()
    serializer_class = MovieAddSerializer