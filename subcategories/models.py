from django.db import models
from django.db.models.deletion import CASCADE
import uuid
from maincategories.models import MainCategory
from datetime import datetime

class SubCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    main_category = models.ForeignKey(MainCategory, on_delete=CASCADE)
    description = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=100, default="PENDING")
    created_by = models.CharField(max_length=100, null=False)
    updated_by = models.CharField(max_length=100, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.CharField(max_length=100, null=True)