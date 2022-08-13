
from django.contrib.auth import views as auth_views
from . import models, forms
from django.contrib.auth import login
from django.shortcuts import render, redirect

class LogIn(auth_views.LoginView):
    template_name = "user_app/login.html"
    redirect_field_name = 'next'	

class LogOut(auth_views.LogoutView):
    template_name = "user_app/logout.html"
    next_page = '/'

def sign_up(request):
    if request.method == 'POST':
        form = forms.UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = forms.UserRegForm()

    return render(request, 'user_app/signup.html', {"form": form})
