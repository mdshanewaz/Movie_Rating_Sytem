from django.urls import path
from Movie_App import views

app_name = 'Movie_App'

urlpatterns = [
    path('list/', views.MovieListAPIView.as_view(), name='movies_list'),
    path('add/', views.MovieAddAPIView.as_view(), name='add_movie'),
    path('<int:pk>/', views.MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie_upfate'),
    path('search/', views.search_movieView, name='search'),
]