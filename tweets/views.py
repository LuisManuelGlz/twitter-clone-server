from .models import Tweet
from .serializers import TweetSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response

class TweetList(generics.ListCreateAPIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer

  def post(self, request, *args, **kwargs):
    serializer = TweetSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)  # Trigger Bad Request if errors exist
    serializer.save(user=request.user)         # Passing the current user
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class TweetDetail(generics.RetrieveDestroyAPIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer
