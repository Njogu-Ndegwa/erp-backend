from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from vendors.models import Vendor
from users.models import User
from location.models import Location
from warehouses.models import Warehouse
from item.models import Item
from toolstates.models import ItemState
from toolbrand.models import ItemBrand
from customer.models import Customer
# Create your models here.
class StockIn(models.Model):
    TOOL = 1
    CONSUMABLE = 2
    TOOLKIT = 3
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    officer = models.CharField(max_length=100, null=False)
    responsible = models.ForeignKey(User, on_delete=CASCADE)
    location = models.ForeignKey(Location, on_delete=CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=CASCADE)
    memo = models.CharField(max_length=100, null=False)
    vehicle = models.CharField(max_length=100, null=False)
    quantity = models.IntegerField(default=0)
    source_bin = models.CharField(max_length=100, null=False)
    brought_by = models.ForeignKey(Customer, on_delete=CASCADE)
    supplier = models.ForeignKey(Vendor, on_delete=CASCADE)
    invoice = models.CharField(max_length=100, null=False)
    lpo = models.CharField(max_length=100, null=True)
    document = models.CharField(max_length=100, null=True)
    delivery_note_number = models.CharField(max_length=100, null=True)
    item = models.ForeignKey(Item, on_delete=CASCADE)
    item_qty = models.IntegerField(default=0)
    cost_per_tool = models.IntegerField(default=0)
    price_per_tool = models.IntegerField(default=0)
    start_milleage = models.CharField(max_length=100)
    stop_milleage = models.CharField(max_length=100)
    callibration = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    states = models.ForeignKey(ItemState, on_delete=CASCADE)
    brands = models.ForeignKey(ItemBrand, on_delete=CASCADE)
    is_deleted = models.BooleanField(default=False)

