from django.urls import path 
from .views import create_and_list_sub_category, edit_and_delete_sub_category

urlpatterns = [
    path('subcategory/', create_and_list_sub_category, name="create_and_list_sub_category"),
    path('subcategory/<uuid:pk>/', edit_and_delete_sub_category, name="edit_and_delete_sub_category"),
]