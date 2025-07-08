# CRUD Operations using Django ORM

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984>


# Retrieve the book
book = Book.objects.get(title="1984")
book.title  # '1984'
book.author  # 'George Orwell'
book.publication_year  # 1949



# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
book.title  # 'Nineteen Eighty-Four'


# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>
