from django.shortcuts import render
from django.views.generic import TemplateView
from . models import Cart, ItemInCart
from items.models import Book
class AddToCart(TemplateView):
    template_name = "orders/cart.html"
    def get_context_data(self, **kwargs):
        cart_id = self.request.session.get('cart')
        item_id = self.request.GET.get('item_id')
        quantity = self.request.GET.get('quantity')

        print(self.request.session.items())
        # 1. get a cart
        if not cart_id:
            if self.request.user.is_anonymous:
                customer = None
            else:
                customer = self.request.user
            cart = Cart.objects.create(
                customer = customer
            )
            self.request.session["cart"] = cart.pk
        else:
            cart = Cart.objects.get(pk=cart_id)
        # 2. add an item to the cart
            item = Book.objects.get(pk=item_id)
            price = item.price * quantity
            item_in_cart, created = ItemInCart.objects.get_or_create(
                cart=cart,
                item=item,
                defaults={
                    'quantity': quantity,
                    'price': price
                }
            )
            if not created:
                item_in_cart.quantity = item_in_cart.quantity + quantity
                item_in_cart.price = item_in_cart.quantity * Book.price
                item_in_cart.save()

        context = super().get_context_data(**kwargs)
        return context
    