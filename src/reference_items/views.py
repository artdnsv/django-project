from django.views import generic
from . import models, forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#Genre
class GenreAdd(LoginRequiredMixin, generic.CreateView):
    template_name = "reference_items/genre_add.html"
    model = models.Genre
    form_class = forms.AddGenreForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy("ref:genre-view", kwargs={'pk' : self.object.pk})

class GenreView(generic.DetailView):
    template_name = "reference_items/genre_view.html"
    model = models.Genre
class GenreList(generic.ListView):
    template_name = "reference_items/genre_list.html"
    model = models.Genre
class GenreEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "reference_items/genre_edit.html"
    model = models.Genre
    form_class = forms.AddGenreForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'

class GenreDelete(LoginRequiredMixin, generic.DeleteView):
    template_name = "reference_items/genre_delete.html"
    model = models.Genre
    form_class = forms.AddGenreForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'

#Author
class AuthorAdd(LoginRequiredMixin, generic.CreateView):
    template_name = "reference_items/author_add.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy("ref:author-view", kwargs={'pk' : self.object.pk})

class AuthorView(generic.DetailView):
    template_name = "reference_items/author_view.html"
    model = models.Author
class AuthorList(generic.ListView):
    template_name = "reference_items/author_list.html"
    model = models.Author
class AuthorEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "reference_items/author_edit.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
class AuthorDelete(LoginRequiredMixin, generic.DeleteView):   
    template_name = "reference_items/author_delete.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'

#Publisher
class PublishereAdd(LoginRequiredMixin, generic.CreateView):
    template_name = "reference_items/publisher_add.html"
    model = models.Publisher
    form_class = forms.AddPublisherForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy("ref:publisher-view", kwargs={'pk' : self.object.pk})
        
class PublisherView(generic.DetailView):
    template_name = "reference_items/publisher_view.html"
    model = models.Publisher   
class PublisherList(generic.ListView):
    template_name = "reference_items/publisher_list.html"
    model = models.Publisher
class PublisherEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "reference_items/publisher_edit.html"
    model = models.Publisher
    form_class = forms.AddPublisherForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
class PublisherDelete(LoginRequiredMixin, generic.DeleteView):
    template_name = "reference_items/publisher_delete.html"
    model = models.Publisher
    form_class = forms.AddPublisherForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
#Series
class SeriesAdd(LoginRequiredMixin, generic.CreateView):
    template_name = "reference_items/series_add.html"
    model = models.Series
    form_class = forms.AddSeriesForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy("ref:series-view", kwargs={'pk' : self.object.pk})

class SeriesView(generic.DetailView):
    template_name = "reference_items/series_view.html"
    model = models.Series
class SeriesList(generic.ListView):
    template_name = "reference_items/series_list.html"
    model = models.Series
class SeriesEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "reference_items/series_edit.html"
    model = models.Series
    form_class = forms.AddSeriesForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
class SeriesDelete(LoginRequiredMixin, generic.DeleteView):
    template_name = "reference_items/series_delete.html"
    model = models.Series
    form_class = forms.AddSeriesForm
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
