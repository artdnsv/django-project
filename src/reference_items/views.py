from django.views import generic
from . import models, forms
from django.urls import reverse_lazy

#Genre
class GenreAdd(generic.CreateView):
    template_name = "reference_items/item_add.html"
    model = models.Genre
    form_class = forms.AddGenreForm

    def get_success_url(self):
        return reverse_lazy("ref:genre-view", kwargs={'pk' : self.object.pk})

class GenreView(generic.DetailView):
    template_name = "reference_items/item_view.html"
    model = models.Genre
class GenreList(generic.ListView):
    template_name = "reference_items/item_list.html"
    model = models.Genre
class GenreEdit(generic.UpdateView):
    template_name = "reference_items/item_edit.html"
    model = models.Genre
class GenreDelete(generic.DeleteView):
    template_name = "reference_items/item_delete.html"
    model = models.Genre
#Author
class AuthorAdd(generic.CreateView):
    template_name = "reference_items/item_add.html"
    model = models.Author
    form_class = forms.AddAuthorForm

    def get_success_url(self):
        return reverse_lazy("ref:author-view", kwargs={'pk' : self.object.pk})

class AuthorView(generic.DetailView):
    template_name = "reference_items/item_view.html"
    model = models.Author
class AuthorList(generic.ListView):
    template_name = "reference_items/item_list.html"
    model = models.Author
class AuthorEdit(generic.UpdateView):
    template_name = "reference_items/item_edit.html"
    model = models.Author
class AuthorDelete(generic.DeleteView):   
    template_name = "reference_items/item_delete.html"
    model = models.Author
#Publisher
class PublishereAdd(generic.CreateView):
    template_name = "reference_items/item_add.html"
    model = models.Publisher
    form_class = forms.AddPublisherForm    

    def get_success_url(self):
        return reverse_lazy("ref:publisher-view", kwargs={'pk' : self.object.pk})
        
class PublisherView(generic.DetailView):
    template_name = "reference_items/item_view.html"
    model = models.Publisher   
class PublisherList(generic.ListView):
    template_name = "reference_items/item_list.html"
    model = models.Publisher
class PublisherEdit(generic.UpdateView):
    template_name = "reference_items/item_edit.html"
    model = models.Publisher
class PublisherDelete(generic.DeleteView):
    template_name = "reference_items/item_delete.html"
    model = models.Publisher
#Series
class SeriesAdd(generic.CreateView):
    template_name = "reference_items/item_add.html"
    model = models.Series
    form_class = forms.AddSeriesForm

    def get_success_url(self):
        return reverse_lazy("ref:series-view", kwargs={'pk' : self.object.pk})

class SeriesView(generic.DetailView):
    template_name = "reference_items/item_view.html"
    model = models.Series
class SeriesList(generic.ListView):
    template_name = "reference_items/item_list.html"
    model = models.Series
class SeriesEdit(generic.UpdateView):
    template_name = "reference_items/item_edit.html"
    model = models.Series
class SeriesDelete(generic.DeleteView):
    template_name = "reference_items/item_delete.html"
    model = models.Series