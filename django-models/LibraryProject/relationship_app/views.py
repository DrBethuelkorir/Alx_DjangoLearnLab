from django.shortcuts import render
from .models import Library, Book
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User


def listallbook(request):
    books = Book.objects.all()
    
    context = {
        'books': books,
    }
    
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailsView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

class signupview(CreateView):
    model = User
    form_class = UserCreationForm
    succeful_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"