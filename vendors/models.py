from django.db import models
import uuid
from datetime import datetime

class Vendor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    mobile = models.CharField(max_length=100, null=False)
    is_deleted = models.BooleanField(default=False)
    description = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.CharField(max_length=100, null=True)
