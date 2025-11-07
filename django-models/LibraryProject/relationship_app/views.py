from django.shortcuts import render
from .models import Library, Book
from django.views.generic import ListView
from django.views.generic.detail import DetailView
def listallbook(request):
    books = Book.objects.all()
    
    context = {
        'books': books,
    }
    
    return render(request, "relationship_app/list_books.html", context)

class LibrarydetailsView(ListView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"