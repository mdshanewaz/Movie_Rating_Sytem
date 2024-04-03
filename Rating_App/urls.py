from django.urls import path
from Rating_App import views

app_name = 'Rating_App'

urlpatterns = [
    path('lists/', views.MovieUserRatingListAPIView.as_view(), name='rating_list'),
    path('update/', views.MovieUserRatingRetrieveUpdateDestroyAPIView.as_view(), name='update_rating'),
]