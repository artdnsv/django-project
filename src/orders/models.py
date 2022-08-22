from types import CellType
from django.db import models
from django.contrib.auth import get_user_model 
from items import models as bk_models
User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='carts',
        verbose_name='Customer',
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True,
        auto_now=False
    )
    updated_date = models.DateTimeField(
        verbose_name='Updated',
        auto_now_add=False,
        auto_now=True
   )

class ItemInCart(models.Model):    
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name='Cart',
    )
    item = models.ForeignKey(
        bk_models.Book,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name='Item',
    )
    quantity = models.SmallIntegerField(
        verbose_name="Quantity",
    ) 
    price = models.DecimalField(
        verbose_name='Price',
        decimal_places=2,
        max_digits=6,
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True,
        auto_now=False
    )
    updated_date = models.DateTimeField(
        verbose_name='Updated',
        auto_now_add=False,
        auto_now=True
   )
    