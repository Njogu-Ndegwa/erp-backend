from rest_framework import serializers
from .models import StockIn


class StockInSerializer(serializers.ModelSerializer):
    """StockIn Serializer"""
    class Meta:
        model = StockIn
        fields = "__all__"