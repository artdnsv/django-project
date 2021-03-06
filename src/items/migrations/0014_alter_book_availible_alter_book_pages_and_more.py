# Generated by Django 4.0.6 on 2022-07-10 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0013_book_instock_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='availible',
            field=models.PositiveIntegerField(verbose_name='Books available'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveSmallIntegerField(verbose_name='Print lenght'),
        ),
        migrations.AlterField(
            model_name='book',
            name='weight',
            field=models.PositiveSmallIntegerField(verbose_name='Item weight(gram)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.PositiveSmallIntegerField(verbose_name='Release date'),
        ),
    ]
