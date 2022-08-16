
from user_app import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
import unicodedata




class UserRegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    class Meta:
        model = models.Account
        fields = "__all__"
USERNAME_FIELD = 'username'       
# fields = ('username','email','password1', 'password2')






# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]