from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    """Vendor Serializer"""
    class Meta:
        model = Vendor
        fields = "__all__"