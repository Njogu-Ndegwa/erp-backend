from django.urls import path 
from .views import create_and_list_location, list_update_delete_location_by_id

urlpatterns = [
    path('location/', create_and_list_location, name="create_and_list_location"),
    path('location/<uuid:pk>/', list_update_delete_location_by_id, name="list_update_delete_location_by_id"),
]