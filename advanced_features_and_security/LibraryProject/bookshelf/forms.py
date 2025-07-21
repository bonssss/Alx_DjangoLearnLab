from django import forms
from .models import Book

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
