from django.shortcuts import render
from .models import Library, Book
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login 

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

class register(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'
    
    def get_success_url(self):
        return reverse_lazy('book_list')  # Where to redirect after successful registration+login
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log the user in automatically
        return HttpResponseRedirect(self.get_success_url())