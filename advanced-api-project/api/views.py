from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world! This is the API index page.")

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class BookDetailView(generics.RetrieveAPIView):
    quesryset =Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]
    
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]