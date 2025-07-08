from bookshelf.models import Book
# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>
