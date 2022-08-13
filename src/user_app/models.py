from enum import unique
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

class Account(models.Model):
    username = models.OneToOneField(
        User,
        verbose_name="Username",
        on_delete=models.CASCADE
    )
    phone_number = PhoneNumberField(
        verbose_name='Phone number',
        unique=True
    )
    birthday = models.DateField( 
        blank=True,
        null=True,
        verbose_name='Birthday',
    )
    gender = models.CharField(
        max_length=6,
        blank=True,
        null=True,
        verbose_name="Gender",
        choices=[('MALE', 'MALE'),('FEMALE', 'FEMALE')]
    )
    country = CountryField(
        verbose_name='Country/Region',
        blank=True,
        null=True,
    )
    city =  models.CharField(
        verbose_name='City/Town',
        max_length=20,
        blank=True,
        null=True
    )
    postcode = models.CharField(
        max_length=6,
        verbose_name='Postcode',
        blank=True,
        null=True
    )
    address1 = models.CharField(
        verbose_name="Address 1",
        max_length=30,
        blank=True,
        null=True      
    )
    address2 = models.CharField(
        verbose_name="Address 2",
        max_length=30,
        blank=True,
        null=True      
    )
    USERNAME_FIELD = 'username'