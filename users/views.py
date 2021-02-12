# from django.contrib.auth.models import User
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework import generics


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
