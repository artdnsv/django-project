from django.views import generic
from django.urls import reverse_lazy
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
import random
from django.db.models.aggregates import Count
from random import randint

# CREATE READ UPDATE DELETE
class ItemAdd(LoginRequiredMixin, generic.CreateView):
    template_name = "items/item_add.html"
    model = models.Book  
    form_class = forms.AddItemForm   
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'

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

class ItemEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "items/item_edit.html"
    model = models.Book
    form_class = forms.AddItemForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy("book:item-list")

class ItemDelete(LoginRequiredMixin, generic.DeleteView):
    template_name = "items/item_delete.html"
    model = models.Book
    success_url = reverse_lazy("book:item-list")
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'


# def get_random():
#     max_id = models.Book.objects.(max_id=Max("id"))['max_id']
#     while True:
#         pk = random.randint(1, max_id)
#         category = models.Book.objects.filter(pk=pk).first()
#         if category:
#             return category

class RandomBook(models.Book):
    def get_random(request):
        randbook = list(models.Book.objects.name())
        book = random.choice(randbook)
        return (request, book)

 