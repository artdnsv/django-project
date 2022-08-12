from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

# class RegisterForm(UserCreationForm):

#     email = forms.EmailField(required=True)

#     name = models.CharField(
#         verbose_name='Name',
#         max_length=25
#     )
#     surname = models.CharField(
#         verbose_name='Surname',
#         max_length=25
#     )
#     phone_number = PhoneNumberField()
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]