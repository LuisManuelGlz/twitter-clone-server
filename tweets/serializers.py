from rest_framework import serializers
from .models import Tweet
from users.serializers import UserSerializer


class TweetSimpleSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta:
    model = Tweet
    fields = ['id', 'content', 'user', 'likes_total', 'created_at']


class TweetSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta:
    model = Tweet
    fields = ['id', 'content', 'user', 'likes', 'created_at']


class TweetLikesSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True)

    class Meta:
        model = Tweet
        fields = ['likes']


class TweetLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['likes_total']
        read_only_fields = ['likes_total']
