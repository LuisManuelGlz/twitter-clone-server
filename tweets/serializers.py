from rest_framework import serializers
from .models import Tweet
from users.serializers import UserSerializer

class TweetSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta:
    model = Tweet
    fields = ['id', 'content', 'user', 'created_at']
