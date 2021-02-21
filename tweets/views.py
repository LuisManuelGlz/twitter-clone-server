from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Tweet
from .serializers import (
    TweetSimpleSerializer,
    TweetSerializer,
    TweetLikesSerializer,
    TweetLikeSerializer
)


class TweetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tweet.objects.all()
    serializer_class = TweetSimpleSerializer

    def post(self, request, *args, **kwargs):
        serializer = TweetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TweetDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tweet.objects.all()
    serializer_class = TweetSimpleSerializer


class LikesDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tweet.objects.all()
    serializer_class = TweetLikesSerializer


class TweetLike(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tweet.objects.all()
    serializer_class = TweetLikeSerializer

    def put(self, request, *args, **kwargs):
        tweet_id = kwargs.get('pk')  # get lookup_field

        user = request.user
        tweet = get_object_or_404(Tweet, pk=tweet_id)

        # check if user exists in tweet likes
        if tweet.likes.filter(id=user.id).exists():
            tweet.likes_total -= 1
            tweet.likes.remove(user)
        else:
            tweet.likes_total += 1
            tweet.likes.add(user)

        tweet.save()

        serializer = TweetLikeSerializer(tweet)
        return Response(serializer.data, status=status.HTTP_200_OK)
