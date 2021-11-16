from rest_framework import serializers
from .models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    """Warehouse Serializer"""
    class Meta:
        model = Warehouse
        fields = "__all__"