from django.urls import path 
from .views import create_new_account, user_login_view, change_password_first_login, refresh_token_view

urlpatterns = [
    path('create-new-account/', create_new_account, name="create_new_account"),
    path('signin/', user_login_view, name="login"),
    path('change-password-first-login/<uuid:pk>/', change_password_first_login, name="change_password_first_login"),
    path('refresh/', refresh_token_view, name="refresh_token_view")

]

