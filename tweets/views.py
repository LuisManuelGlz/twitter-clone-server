from .models import Tweet
from .serializers import TweetSerializer
from rest_framework import generics

class TweetList(generics.ListCreateAPIView):
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer

class TweetDetail(generics.RetrieveDestroyAPIView):
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer
