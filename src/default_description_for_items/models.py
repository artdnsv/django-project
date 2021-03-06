from django.db import models

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Genre',
        max_length=25
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    
class Publisher(models.Model):
    name = models.CharField(
        verbose_name='Publisher',
        max_length=25
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    
class Series(models.Model):
    name = models.CharField(
        verbose_name='Series',
        max_length=25
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    
class Autor(models.Model):
    name = models.CharField(
        verbose_name='Author',
        max_length=25
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
