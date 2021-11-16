from django.urls import path 
from .views import create_and_list_item, list_update_delete_item_by_id

urlpatterns = [
    path('item/', create_and_list_item, name="create_and_list_item"),
    path('item/<uuid:pk>/', list_update_delete_item_by_id, name="list_update_delete_item_by_id"),
]