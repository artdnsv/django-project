from django.forms import ModelForm
from items import models

class AddItemForm (ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
