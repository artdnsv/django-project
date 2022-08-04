from django.forms import ModelForm
from . import models

class AddGenreForm (ModelForm):
    class Meta:
        model = models.Genre
        fields = "__all__"

class AddAuthorForm (ModelForm):
    class Meta:
        model = models.Author
        fields = "__all__"

class AddPublisherForm (ModelForm):
    class Meta:
        model = models.Publisher
        fields = "__all__"

class AddSeriesForm (ModelForm):
    class Meta:
        model = models.Series
        fields = "__all__"