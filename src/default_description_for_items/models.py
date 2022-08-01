from django.db import models

class Genre(models.Model):
    name = models.CharField(
        max_length=25,
        verbose_name= "Genre",
        )
    def __str__(self) -> str:
        return self.name
    
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
class Author(models.Model):
    name = models.CharField(
    verbose_name= "Author",
    max_length=25,

    )
    def __str__(self) -> str:
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(
        verbose_name="Publisher",
        max_length=25,
        )
    def __str__(self) -> str:
        return self.name
    
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    
class Series(models.Model):
    name = models.CharField(
        verbose_name="Series",
        max_length=25
    )
    def __str__(self) -> str:
        return self.name
    
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    
