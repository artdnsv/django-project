from django.db import models

class Genre(models.Model):
    name = models.CharField(
        max_length=25,
        verbose_name= "Genre",
        unique=True
        )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return self.name

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
        unique=True
        )

    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return self.name
    
class Series(models.Model):
    name = models.CharField(
        verbose_name="Series",
        max_length=25
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True,
        unique=True

    )
    def __str__(self) -> str:
        return self.name
    
