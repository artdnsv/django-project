# Generated by Django 4.0.6 on 2022-07-10 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0015_book_dimensions_alter_book_price_alter_book_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.CharField(choices=[('Hard', 'Hardcover'), ('Soft', 'Paperback')], max_length=30, verbose_name='Book type'),
        ),
    ]
