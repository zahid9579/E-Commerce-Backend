from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.views import  APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allows public access for registration

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Creates user

            # Generates JWT tokens for the newly registered user
            refresh = RefreshToken.for_user(user)

            return Response({
                'msg': "User Registeration Successfully!",
                "User": serializer.data,
                'refresh': str(refresh),  # Send refresh token
                "access": str(refresh.access_token)  #  Send access token
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

# Login User 
class LoginView(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "msg": "Logged In!",
                "refresh": str(refresh),
                "access": str(refresh.access_token)
                }, status=status.HTTP_200_OK)
        return Response({"msg": "Login failed, user credentials were not correct"}, status=status.HTTP_400_BAD_REQUEST)
        
      
        
        
# LogOut User
class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'msg': "Logout Successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
       
    
