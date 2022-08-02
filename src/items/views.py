from django.views import generic
from django.urls import reverse_lazy
from . import models, forms
# CREATE READ UPDATE DELETE
class HomePage(generic.TemplateView):
     template_name = "items/home.html"
     def get_context_data(self, *args, **kwargs): 
         return super().get_context_data(**kwargs)

class ItemAdd(generic.CreateView):
    template_name = "items/item_add.html"
    model = models.Book  
    form_class = forms.AddItemForm
    
    def get_success_url(self) :
        return f"item/<{self.object.pk}>/"

class ItemView(generic.DetailView):
    template_name = "items/item_view.html"
    model = models.Book

class ItemList(generic.ListView):
    template_name = "items/item_list.html"
    model = models.Book

class ItemDelete(generic.DeleteView):
    template_name = "items/item_delete.html"
    model = models.Book
    success_url = "/item-list/"



# def item_view(request, id):
#     item = models.Book.objects.get(pk=id)
#     out = f'''
#     ID: {item.pk} </br>
#     Name of the item: {item.name} </br>
#     Genre: {item.genre} </br>
#     Authors: {item.author} </br>
#     Publisher: {item.publisher} </br>
#     Series: {item.series} </br>
#     Price: {item.price} руб. </br>
#     Release year: {item.year} </br>
#     Print lenght: {item.pages} </br>
#     Cover: {item.cover} </br>
#     Format: {item.dimensions} </br>
#     ISBN: {item.isbn} </br>
#     Weight: {item.weight} </br>
#     In stock: {item.instock} </br>
#     Reading age: {item.age} </br>
#     Books availible: {item.availible} </br>
#     Rating: {item.rating} </br>
#     Date of cataloging: {item.cataloging_date} </br>
#     Changing date: {item.changing_date} </br>
#     '''
#     return HttpResponse(out)

 