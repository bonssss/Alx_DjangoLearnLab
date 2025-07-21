import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  # Replace with your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author.name}: {[book.title for book in books]}")
    except Author.DoesNotExist:
        print("Author not found.")

# 2. List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library.name}: {[book.title for book in books]}")
    except Library.DoesNotExist:
        print("Library not found.")

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # <-- REQUIRED LINE
        print(f"Librarian for {library.name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Librarian or Library not found.")


# Run queries
query_books_by_author("Chinua Achebe")
list_books_in_library("Central Library")
get_librarian_for_library("Central Library")
