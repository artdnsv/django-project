from django.http import HttpResponse
from django.shortcuts import render
from . import models

def item_view(request):
    item = models.Book.objects.get(pk=1)
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