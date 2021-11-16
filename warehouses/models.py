from datetime import datetime
from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from location.models import Location

class Warehouse(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    location = models.ForeignKey(Location, on_delete=CASCADE)
    description = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=100, default="PENDING")
    created_by = models.CharField(max_length=100, null=False)
    updated_by = models.CharField(max_length=100, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.CharField(max_length=100, null=True)