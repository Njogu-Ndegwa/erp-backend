from django.urls import path 
from .views import create_and_list_main_category, list_update_delete_main_category_by_id

urlpatterns = [
    path('main-category/', create_and_list_main_category, name="create_and_list_maincategory"),
    path('main-category/<uuid:pk>/', list_update_delete_main_category_by_id, name="list_update_delete_maincategory_by_id"),
]