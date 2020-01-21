from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .serializers import UserSerializer



class SignUpAPIView(CreateAPIView):
    serializer_class = UserSerializer



    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

