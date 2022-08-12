from django.urls import path
from . import views

app_name = "user_app"

urlpatterns = [
    path('login/', views.LogIn.as_view(), name="login"),
    path('auth_modal/', views.LogIn.as_view(), name="auth_modal"),
    path('logout/', views.LogOut.as_view(), name="logout")
    ]