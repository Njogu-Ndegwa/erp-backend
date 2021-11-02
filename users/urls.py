from django.urls import path 
from .views import create_new_account, user_login_view

urlpatterns = [
    path('create-new-account/', create_new_account, name="create_new_account"),
     path('login/', user_login_view, name="login"),
]

