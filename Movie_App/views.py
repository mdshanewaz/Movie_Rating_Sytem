from django.shortcuts import render
from django.db.models import Avg

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
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

@api_view(['GET'])
def search_movieView(request):
    query = request.query_params.get('query', '')
    movies = MovieModel.objects.filter(name__icontains=query)

    if movies.exists():
        serializer = MovieSerializer(movies, many=True)
        average_rating = movies.aggregate(Avg('rating__rating'))['rating__rating__avg']
        return Response({'movies': serializer.data, 'average_rating': average_rating})
    else:
        return Response({'message': 'No movies found'}, status=status.HTTP_404_NOT_FOUND)