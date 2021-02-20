from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import User, Profile


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'date_joined'
        ]


class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'avatar',
            'location',
            'bio',
            'website',
            'following_total',
            'followers_total',
            'birth_date',
        ]
        read_only_fields = ['following_total', 'followers_total']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSimpleSerializer()

    class Meta:
        model = Profile
        fields = [
            'avatar',
            'location',
            'bio',
            'website',
            'following_total',
            'followers_total',
            'birth_date',
            'user'
        ]


class ProfileFollowingSerializer(serializers.ModelSerializer):
    following = ProfileSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['following']


class ProfileFollowersSerializer(serializers.ModelSerializer):
    followers = ProfileSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['followers']


class ProfileFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['followers_total']
        read_only_fields = ['followers_total']


class FollowingSerializer(serializers.ModelSerializer):
    profile = ProfileFollowingSerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'profile']


class FollowersSerializer(serializers.ModelSerializer):
    profile = ProfileFollowersSerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'profile']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSimpleSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'profile',
            'date_joined'
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

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                'Your username must be longer than 4 characters.')
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
