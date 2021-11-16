from django.urls import path 
from .views import create_and_list_customer, list_update_delete_customer_by_id

urlpatterns = [
    path('customer/', create_and_list_customer, name="create_and_list_customer"),
    path('customer/<uuid:pk>/', list_update_delete_customer_by_id, name="list_update_delete_customer_by_id"),
]