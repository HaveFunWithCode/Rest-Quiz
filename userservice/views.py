from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .serializers import UserSerializer



class SignUpAPIView(CreateAPIView):
    serializer_class = UserSerializer


    def get(self,request,format=None):
        API_manual="""
        your input format to sign up should be like below 
            {
            "username":"zahra",
            "first_name":"zahra",
            "last_name":"mohammadi",
            "email":"zahra@gmail.com",
            "password":"123456",
            "confirm_password":"123456",
            "profile":{
                "birth_date":"1988-02-02"
            }
            } 
        """
        return Response({'API_manual':API_manual})
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(ObtainAuthToken):
    """ Handle creating or get user authentication tokens"""

    renderer_classes =api_settings.DEFAULT_RENDERER_CLASSES

    def get(self,request):
        API_manual="""
        your input format to login should be like below
        {
            "username":"zahra",
            "password":"123456"
        }
        """
        return Response({"API_manual":API_manual})

    def post(self,request):

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})



