from django.urls import path 
from .views import create_and_list_item_brand, list_update_delete_item_brand_by_id

urlpatterns = [
    path('item-brand/', create_and_list_item_brand, name="create_and_list_item_brand"),
    path('item-brand/<uuid:pk>/', list_update_delete_item_brand_by_id, name="list_update_delete_item_brand_by_id"),
]