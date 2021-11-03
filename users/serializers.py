from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password


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


class ChangePasswordSerializer(serializers.ModelSerializer):
    """Force the user to change password on initial login"""
    new_password = serializers.CharField(write_only=True, required=True,
                                         validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'new_password', 'new_password2')

    def validate(self, attrs):
        """Check whether the new passwords match before saving"""

        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({
                "password": "Password fields didn't match."})
        return attrs
