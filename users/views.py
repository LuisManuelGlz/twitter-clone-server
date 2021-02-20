from .models import User, Profile
from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    FollowingSerializer,
    FollowersSerializer,
    ProfileFollowSerializer
)
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class FollowingDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = FollowingSerializer
    lookup_field = 'username'


class FollowerDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = FollowersSerializer
    lookup_field = 'username'


class ProfileFollow(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileFollowSerializer
    lookup_field = 'user_id'

    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')  # get lookup_field

        follower_profile = Profile.objects.get(user=request.user)
        followed_profile = Profile.objects.get(pk=user_id)

        # check if followed profile exists in follower profile
        if follower_profile.following.filter(pk=user_id).exists():
            follower_profile.following_total -= 1
            follower_profile.following.remove(followed_profile)

            followed_profile.followers_total -= 1
            followed_profile.followers.remove(follower_profile)
        else:
            follower_profile.following_total += 1
            follower_profile.following.add(followed_profile)

            followed_profile.followers_total += 1
            followed_profile.followers.add(follower_profile)

        follower_profile.save()
        followed_profile.save()

        serializer = ProfileFollowSerializer(followed_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
