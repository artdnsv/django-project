from datetime import datetime
from django.urls import reverse_lazy
from django.views import generic
from . import models, forms
from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    items = models.Book.objects.all()
    return render(request, template_name="items/item_list.html", context={"items":items})

def item_view(request, id):
    item = models.Book.objects.get(pk=id)
    out = f'''
    ID: {item.pk} </br>
    Name of the item: {item.name} </br>
    Genre: {item.genre} </br>
    Authors: {item.author} </br>
    Publisher: {item.publisher} </br>
    Series: {item.series} </br>
    Price: {item.price} руб. </br>
    Release year: {item.year} </br>
    Print lenght: {item.pages} </br>
    Cover: {item.cover} </br>
    Format: {item.dimensions} </br>
    ISBN: {item.isbn} </br>
    Weight: {item.weight} </br>
    In stock: {item.instock} </br>
    Reading age: {item.age} </br>
    Books availible: {item.availible} </br>
    Rating: {item.rating} </br>
    Date of cataloging: {item.cataloging_date} </br>
    Changing date: {item.changing_date} </br>
    '''
    return HttpResponse(out)

class ItemAdd(generic.CreateView):
    template_name = "items/item_add.html"
    model = models.Book
    form_class = forms.AddItemForm

    def get_success_url(self) -> str:
        return reverse_lazy("items:item-view", kwargs={'id' : self.object.pk})  
 