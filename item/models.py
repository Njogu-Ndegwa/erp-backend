from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from maincategories.models import MainCategory
from subcategories.models import SubCategory
from datetime import datetime

# Create your models here.
class Item(models.Model):
    TOOL = 1
    CONSUMABLE = 2
    TOOLKIT = 3
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name= models.CharField(max_length=100, null=False)
    authorize = models.BooleanField(default=False)
    type = models.PositiveBigIntegerField(choices=((TOOL, "TOOL"), (CONSUMABLE, "CONSUMABLE"), (TOOLKIT, "TOOLKIT")),default=TOOL)
    code = models.CharField(max_length=100, null=False)
    serial = models.CharField(max_length=100, null=False)
    image_url = models.CharField(max_length=100, null=False)
    is_deleted = models.BooleanField(default=False)
    main_category = models.ForeignKey(MainCategory, on_delete=CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=CASCADE)
    unit = models.CharField(max_length=100, null=False)
    o_quantity = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    status = models.CharField(max_length=100, default="PENDING")
    created_by = models.CharField(max_length=100, null=False)
    updated_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.CharField(max_length=100, null=True)