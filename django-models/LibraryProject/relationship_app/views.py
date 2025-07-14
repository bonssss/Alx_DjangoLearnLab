from django.shortcuts import render
# from django.template import Library
from relationship_app.models import Book
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})



class LibraryDetailView(DetailView):
    model =Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'