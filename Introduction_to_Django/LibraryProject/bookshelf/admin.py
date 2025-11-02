from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters in the sidebar
    list_filter = ('author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')
    
    # Optional: Fields to use for autocomplete (Django 2.0+)
    search_help_text = "Search by title or author"
    
    # Optional: Number of items per page in admin
    list_per_page = 25
    
    # Optional: Ordering in admin
    ordering = ('title',)