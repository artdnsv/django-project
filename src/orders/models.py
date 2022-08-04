from django.db import models
from django.contrib.auth import get_user_model 
from items import models 
User = get_user_model()

# class Cart(models.Model):
#     customer = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         related_name='carts',
#         verbose_name='Customer',
#         null=True,
#         blank=True
#     )
#     created_date = models.DateTimeField(
#         verbose_name='Created',
#         auto_created=True,
#         auto_now=False
#     )
#     updated_date = models.DateTimeField(
#         verbose_name='Updated',
#         auto_created=False,
#         auto_now=True
#    )

# class ItemInCart(models.Model):    cart = 
