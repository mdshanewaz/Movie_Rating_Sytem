from django.urls import path
from Login_App import views

app_name = 'Login_App'

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('users/', views.UserProfileAPIView.as_view(), name='users'),
]