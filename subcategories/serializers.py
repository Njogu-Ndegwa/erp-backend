from rest_framework import serializers
from .models import SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    """SubCategory Serializer"""
    class Meta:
        model = SubCategory
        fields = "__all__"