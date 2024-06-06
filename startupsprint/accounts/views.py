from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


class UserInfo(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer