from django.urls import path 
from .views import create_and_list_stock_in, list_update_delete_stock_in_by_id

urlpatterns = [
    path('stock-in/', create_and_list_stock_in, name="create_and_list_stock_in"),
    path('stock-in/<uuid:pk>/', list_update_delete_stock_in_by_id, name="list_update_delete_stock_in_by_id"),
]