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
    
    def get_success_url(self):
        return reverse_lazy("book:item-list")

class ItemList(generic.ListView):
    template_name = "items/item_list.html"
    model = models.Book

class ItemView(generic.DetailView):
    template_name = "items/item_view.html"
    model = models.Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy("items:item-view", kwargs={'pk' : self.object.pk})

class ItemEdit(generic.UpdateView):
    template_name = "items/item_edit.html"
    model = models.Book
    form_class = forms.AddItemForm
    def get_success_url(self):
        return reverse_lazy("book:item-list")

class ItemDelete(generic.DeleteView):
    template_name = "items/item_delete.html"
    model = models.Book
    success_url = reverse_lazy("book:item-list")




 