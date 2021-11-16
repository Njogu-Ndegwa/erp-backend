from rest_framework import serializers
from .models import ItemBrand


class ItemBrandSerializer(serializers.ModelSerializer):
    """ItemBrand Serializer"""
    class Meta:
        model = ItemBrand
        fields = "__all__"