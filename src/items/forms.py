from django import forms
from items import models

class AddItemForm (forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
