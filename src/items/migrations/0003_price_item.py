# Generated by Django 4.0.6 on 2022-07-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_name_price_delete_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='item',
            field=models.CharField(default='жук', max_length=200),
            preserve_default=False,
        ),
    ]
