import requests
import random
from django import template
from items.models import Book
from django.db.models import Max

register = template.Library()

@register.simple_tag
def view_rates():
    data = requests.get('https://www.nbrb.by/api/exrates/rates/431').json()
   #  data = data['Cur_OfficialRate']
    return data['Cur_OfficialRate']
    
# @register.simple_tag
# def get_random():
#     return Book.objects.name.order_by("?").first()

@register.simple_tag
def get_random_book():
    max_id = Book.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        book = Book.objects.filter(pk=pk).first()
        if book:
            return book.name