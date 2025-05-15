from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.views import  APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate


# Create your views here.

# Signu/Register User
class RegisterView(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "User Registeration Successfully!", "User": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )
        
        

# Login User 
class LoginView(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            return Response({"msg": "Logged In!"}, status=status.HTTP_200_OK)
        return Response({"msg": "Login failed, user credetials were not correct"}, status=status.HTTP_400_BAD_REQUEST)
        
        
# LogOut User
class LogoutView(APIView):
    authentication_classes=[IsAuthenticated]
    
    def get(self, request):
        # request.user.delete()
        return Response({"msg": "Logout Successfully"}, status=status.HTTP_200_OK)
    
    
