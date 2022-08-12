from importlib.resources import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.shortcuts import resolve_url

class LogIn(auth_views.LoginView):
    template_name = "user_app/login.html"
    redirect_field_name = 'next'	
    # def get_success_url(self):
    #     return self.get_redirect_url()

    # def get_redirect_url(self):
    #     redirect_to = self.request.POST.get(
    #     self.redirect_field_name,
    #     self.request.GET.get(self.redirect_field_name, '')
    #     )
    #     return redirect_to 

class LogOut(auth_views.LogoutView):
    template_name = "user_app/logout.html"
    next_page = '/'
