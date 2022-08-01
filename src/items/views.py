from django.http import HttpResponse
from django.shortcuts import render

from default_description_for_items.models import Genre
from . import models

def item_list(request):
    items = models.Book.objects.all()
    return render(request, template_name="items/item_list.html", context={"items":items})

def item_view(request, id):
    print(id)
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

def item_add(request):
    out = '''
    <form action="">
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value="John"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value="Doe"><br>
        <button type="submit">Submit</button>
    </form>
    '''
    return HttpResponse(out)