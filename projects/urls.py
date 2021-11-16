from django.urls import path 
from .views import create_and_list_project, list_update_delete_project_by_id

urlpatterns = [
    path('project/', create_and_list_project, name="create_and_list_project"),
    path('project/<uuid:pk>/', list_update_delete_project_by_id, name="list_update_delete_project_by_id"),
]