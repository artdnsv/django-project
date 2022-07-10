from tabnanny import verbose
from django.db import models
from isbn_field import ISBNField

# Create your models here.

class Name(models.Model):
    name = models.CharField(
        verbose_name='Name of the item',
        max_length=25
    )
    
class Price(models.Model):
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=10, 
        decimal_places=2
        )
    def __str__(self):
        return str(self.price) + " BYN"
    
class YearOfPublication(models.Model):
    year = models.PositiveSmallIntegerField(
        verbose_name="Release"
    )

class Page(models.Model):
    pages = models.PositiveSmallIntegerField(
        verbose_name="Print lenth"
    )
    def __str__(self):
        return str(self.pages) + " pages"
    

class Format(models.Model):
    CHOICES = (
        ('Hard',"Hardcover"),
        ('Soft',"Paperback")
    )
    cover = models.CharField(
        max_length=30,
        verbose_name="Format",
        choices=CHOICES 
    )
    
class ISBN(models.Model):
    isbn = ISBNField()
    
class Weight(models.Model):
    weight = models.PositiveSmallIntegerField(
        verbose_name='Item weight'
    )
    def __str__(self):
        return str(self.weigt) + " gram"

class InStock(models.Model):
    CHOICES = (
        ('Y',"Yes"),
        ('N',"No")
    )
    cover = models.CharField(
        max_length=30,
        verbose_name="In stock",
        choices=CHOICES 
    )
class ReadingAge(models.Model):
    age = models.CharField(
        verbose_name="Reading Age",
        max_length=3
    )
    
    