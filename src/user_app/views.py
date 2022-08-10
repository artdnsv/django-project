
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views

class LoginView(auth_views.LoginView):
    template_name="user_app/login.html"