from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    """Location Serializer"""
    class Meta:
        model = Location
        fields = "__all__"