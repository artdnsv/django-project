# Generated by Django 4.0.6 on 2022-08-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_book_delete_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='availible',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Books available'),
        ),
    ]
