# Generated by Django 4.0.6 on 2022-08-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_items', '0002_author_delete_autor_alter_genre_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=25, unique=True, verbose_name='Series'),
        ),
    ]
