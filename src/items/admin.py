from django.contrib import admin
from . import models

admin.site.register(models.Name)
admin.site.register(models.Price)
admin.site.register(models.YearOfPublication)
admin.site.register(models.Format)
admin.site.register(models.Page)
admin.site.register(models.ISBN)
admin.site.register(models.Weight)
admin.site.register(models.InStock)
admin.site.register(models.ReadingAge)
