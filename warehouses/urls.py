from django.urls import path 
from .views import create_and_list_warehouse, list_update_delete_warehouse_by_id

urlpatterns = [
    path('warehouse/', create_and_list_warehouse, name="create_and_list_warehouse"),
    path('warehouse/<uuid:pk>/', list_update_delete_warehouse_by_id, name="list_update_delete_warehouse_by_id"),
]