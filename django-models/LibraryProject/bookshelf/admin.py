from django.contrib import admin
from .models import Book

# Register your models here.

admin.site.site_header = "Library Project Admin"
# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'publication_year')
    list_filter = ('publication_year',)
    # ordering = ('-published_date',)

