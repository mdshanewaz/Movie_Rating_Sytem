from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from Login_App.models import ProfileModel
from Login_App.serializers import UserLoginSerializer, UserProfileSerializer

# Create your views here.

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({'token': user.auth_token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileAPIView(APIView):
    permission_class = [IsAuthenticated]

    def get(self, request):
        profiles = ProfileModel.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)