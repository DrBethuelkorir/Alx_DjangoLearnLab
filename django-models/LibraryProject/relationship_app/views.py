from django.shortcuts import render
from relationship_app.models import Book,Library
from django.views.generic import ListView
def listallbook(request):
    books = Book.objects.all()
    
    context = {
        'books': books,
    }
    
    return render(request, "relationship_app/list_books.html", context)

class Librarydetails(ListView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"