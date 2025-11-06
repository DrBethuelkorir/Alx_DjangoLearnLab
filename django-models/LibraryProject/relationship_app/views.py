from django.shortcuts import render
from relationship_app.models import Book

def listallbook(request):
    books = Book.objects.all()
    
    context = {
        'books': books
    }
    
    return render(request, "list_books.html", context)