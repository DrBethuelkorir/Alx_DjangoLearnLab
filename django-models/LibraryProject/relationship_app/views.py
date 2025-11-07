from django.shortcuts import render
from relationship_app.models import Book, Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView

def listallbook(request):
    books = Book.objects.all()
    
    context = {
        'books': books,
    }
    
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):  # Renamed from Librarydetails to LibraryDetailView
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books from this specific library to the context
        context['books'] = self.object.books.all()  # This gets books for the specific library
        return context