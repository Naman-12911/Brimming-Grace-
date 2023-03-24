from .serializer import UserSerializers,UserLoginSerializer
from rest_framework.response import Response
from .models import User # import models
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

# register the user
class Register(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializers
    # renderer_classes = (UserRenderer,)
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
       # token = RefreshToken.for_user(user).access_token
        return Response(user_data, status=status.HTTP_201_CREATED)
    
# login apis
class Login(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)