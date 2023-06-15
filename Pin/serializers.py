from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Pin
from user.serializers import UserPorfileSerializer, UserSerializer



class PostSerializer(serializers.ModelSerializer):

    postedBy = UserSerializer()
    postedByProfile = UserPorfileSerializer()

    class Meta:
        model = Pin
        fields = ['id', 'title', 'slug', 'content', 'image', 'published_date', 'likes', 'updated', 'postedByProfile', 'postedBy']
