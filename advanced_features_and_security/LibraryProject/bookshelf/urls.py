from django.urls import path
from .views import book_list, example_form_view

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('example-form/', example_form_view, name='example_form'),
]
