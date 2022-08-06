from django.views import generic
from . import models, forms
from django.urls import reverse_lazy

#Genre
class GenreAdd(generic.CreateView):
    template_name = "reference_items/genre_add.html"
    model = models.Genre
    form_class = forms.AddGenreForm

    def get_success_url(self):
        return reverse_lazy("ref:genre-view", kwargs={'pk' : self.object.pk})

class GenreView(generic.DetailView):
    template_name = "reference_items/genre_view.html"
    model = models.Genre
class GenreList(generic.ListView):
    template_name = "reference_items/genre_list.html"
    model = models.Genre
class GenreEdit(generic.UpdateView):
    template_name = "reference_items/genre_edit.html"
    model = models.Genre
    form_class = forms.AddGenreForm    
class GenreDelete(generic.DeleteView):
    template_name = "reference_items/genre_delete.html"
    model = models.Genre
    form_class = forms.AddGenreForm

#Author
class AuthorAdd(generic.CreateView):
    template_name = "reference_items/author_add.html"
    model = models.Author
    form_class = forms.AddAuthorForm

    def get_success_url(self):
        return reverse_lazy("ref:author-view", kwargs={'pk' : self.object.pk})

class AuthorView(generic.DetailView):
    template_name = "reference_items/author_view.html"
    model = models.Author
class AuthorList(generic.ListView):
    template_name = "reference_items/author_list.html"
    model = models.Author
class AuthorEdit(generic.UpdateView):
    template_name = "reference_items/author_edit.html"
    model = models.Author
    form_class = forms.AddAuthorForm
class AuthorDelete(generic.DeleteView):   
    template_name = "reference_items/author_delete.html"
    model = models.Author
    form_class = forms.AddAuthorForm

#Publisher
class PublishereAdd(generic.CreateView):
    template_name = "reference_items/publisher_add.html"
    model = models.Publisher
    form_class = forms.AddPublisherForm    

    def get_success_url(self):
        return reverse_lazy("ref:publisher-view", kwargs={'pk' : self.object.pk})
        
class PublisherView(generic.DetailView):
    template_name = "reference_items/publisher_view.html"
    model = models.Publisher   
class PublisherList(generic.ListView):
    template_name = "reference_items/publisher_list.html"
    model = models.Publisher
class PublisherEdit(generic.UpdateView):
    template_name = "reference_items/publisher_edit.html"
    model = models.Publisher
    form_class = forms.AddPublisherForm
class PublisherDelete(generic.DeleteView):
    template_name = "reference_items/publisher_delete.html"
    model = models.Publisher
    form_class = forms.AddPublisherForm
#Series
class SeriesAdd(generic.CreateView):
    template_name = "reference_items/series_add.html"
    model = models.Series
    form_class = forms.AddSeriesForm

    def get_success_url(self):
        return reverse_lazy("ref:series-view", kwargs={'pk' : self.object.pk})

class SeriesView(generic.DetailView):
    template_name = "reference_items/series_view.html"
    model = models.Series
class SeriesList(generic.ListView):
    template_name = "reference_items/series_list.html"
    model = models.Series
class SeriesEdit(generic.UpdateView):
    template_name = "reference_items/series_edit.html"
    model = models.Series
    form_class = forms.AddSeriesForm
class SeriesDelete(generic.DeleteView):
    template_name = "reference_items/series_delete.html"
    model = models.Series
    form_class = forms.AddSeriesForm
