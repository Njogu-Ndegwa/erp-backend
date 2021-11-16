from django.urls import path 
from .views import create_and_list_vendor, list_update_delete_vendor_by_id

urlpatterns = [
    path('vendor/', create_and_list_vendor, name="create_and_list_vendor"),
    path('vendor/<uuid:pk>/', list_update_delete_vendor_by_id, name="list_update_delete_vendor_by_id"),
]