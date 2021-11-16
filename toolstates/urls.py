from django.urls import path 
from .views import create_and_list_item_state, list_update_delete_item_state_by_id

urlpatterns = [
    path('item-state/', create_and_list_item_state, name="create_and_list_item_state"),
    path('item-state/<uuid:pk>/', list_update_delete_item_state_by_id, name="list_update_delete_item_state_by_id"),
]