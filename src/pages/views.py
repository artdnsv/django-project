from datetime import datetime, timedelta
from django.shortcuts import render
from django.views import generic
from items import models
# Create your views here.

five_days = timedelta(days=5)
class HomePage(generic.TemplateView):
     template_name = "pages/home_page.html"

     def get_context_data(self, *args, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now().date
        context['city_list'] = models.Book.objects.filter(cataloging_date__gt=datetime.now() - five_days)
        context['author_list'] = models.Author.objects.all()[:5]
