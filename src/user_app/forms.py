
from user_app import models
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = models.Account
        fields = "__all__"
# fields = ('username','email','password1', 'password2')






# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]