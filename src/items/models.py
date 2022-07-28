from tabnanny import verbose
from django.db import models
from isbn_field import ISBNField
from default_description_for_items.models import *

# Create your models here.

class Book(models.Model):
    name = models.CharField(
        verbose_name='Name of the item',
        max_length=25
    )
    def __str__(self):
        return 'id' + ' ' + str(self.pk) + ' — ' + str(self.name) + ' | ' + str(self.author)
    
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Genres',
        related_name='genres',
        
        )
    
    author = models.ManyToManyField(
        Author,
        verbose_name='Authors',
        related_name='authors'
        )
    
    
    publisher = models.ForeignKey(
        Publisher,
        related_name='publishers',
        on_delete=models.PROTECT
    )
    
    series = models.ForeignKey(
        Series,
        related_name='series',
        on_delete=models.PROTECT
    )
    
    
    price = models.DecimalField(
        verbose_name='Price(BYN)',
        max_digits=10, 
        decimal_places=2
        )
    
    year = models.PositiveSmallIntegerField(
        verbose_name="Release year"
    )
    
    pages = models.PositiveSmallIntegerField(
        verbose_name="Print lenght (pages)"
    )
    
    CHOICES = (
        ('Hard',"Hardcover"),
        ('Soft',"Paperback"),
    )
    cover = models.CharField(
        verbose_name="Book type",
        max_length=30,
        choices=CHOICES 
    )
    dimensions = models.CharField(
        verbose_name="Dimensions",
        max_length=25
    )
    isbn = ISBNField()
    
    weight = models.PositiveSmallIntegerField(
        verbose_name='Item weight(gram)'
    )
    
    OPTIONS = (
        ('y',"Yes"),
        ('n',"No")
    )
    instock = models.CharField(
        max_length=30,
        verbose_name="In stock",
        choices=OPTIONS 
    )
    
    age = models.CharField(
        verbose_name="Reading Age",
        max_length=3
    )

    availible = models.PositiveIntegerField(
        verbose_name="Books available"
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="Rating (0-10)",
    )
    
    cataloging_date = models.DateTimeField(
        verbose_name="Date of cataloging",
        auto_now_add=True,
        
    )
    changing_date = models.DateTimeField(
        verbose_name="Changing date",
        auto_now=True
    )
    