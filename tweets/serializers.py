from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  content = serializers.CharField(max_length=280)
  created = serializers.DateTimeField(read_only=True)

  def create(self, validated_data):
    """
    Create and return a new `Tweet` instance, given the validated data.
    """
    return Tweet.objects.create(**validated_data)
