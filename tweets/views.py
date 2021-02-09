from .models import Tweet
from .serializers import TweetSerializer
from rest_framework import generics, permissions

class TweetList(generics.ListCreateAPIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer

class TweetDetail(generics.RetrieveDestroyAPIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer
