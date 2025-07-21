from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm, BookForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data safely here
            messages.success(request, "Form submitted successfully!")
            return redirect('example_form')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
