# Generated by Django 4.0.6 on 2022-07-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_book_delete_format_delete_instock_delete_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], max_length=30, verbose_name='In stock'),
        ),
    ]
