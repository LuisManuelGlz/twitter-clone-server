from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = [
      'avatar',
      'location',
      'bio',
      'website',
      'birth_date'
    ]

class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer()

  class Meta:
    model = User
    fields = [
      'id',
      'name',
      'username',
      'profile',
      'created_at'
    ]
    read_only_fields = ['username']

  def update(self, instance, validated_data):
    profile_data = validated_data.pop('profile')
    profile = instance.profile

    instance.name = validated_data.get('name', instance.name)
    instance.save()

    profile.location = profile_data.get('location', profile.location)
    profile.bio = profile_data.get('bio', profile.bio)
    profile.website = profile_data.get('website', profile.website)
    profile.birth_date = profile_data.get('birth_date', profile.birth_date)
    profile.save()

    return instance

class UserCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'name',
      'username',
      'email',
      'password',
    ]
    extra_kwargs = {
      'email': {'write_only': True},
      'password': {'write_only': True}
    }