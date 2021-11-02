from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    """User Serializer"""

    class Meta:
        model=User
        fields= "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', )


class UserLoginSerializer(serializers.ModelSerializer):
    """Login Serializer class"""
    email = serializers.EmailField(max_length=255, min_length=10)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    groups = GroupSerializer(many=True)

    class Meta:
        """Response should have this fields"""
        model = User
        fields = "__all__" 
