from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.views import  APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status


# Create your views here.
class RegisterView(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        pass
