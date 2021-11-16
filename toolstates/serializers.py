from rest_framework import serializers
from .models import ItemState


class ItemStateSerializer(serializers.ModelSerializer):
    """ItemState Serializer"""
    class Meta:
        model = ItemState
        fields = "__all__"