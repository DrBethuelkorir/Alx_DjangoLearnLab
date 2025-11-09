from django.shortcuts import render
from .models import Library, Book
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login 
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test

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
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    
    def get_success_url(self):
        return reverse_lazy('book_list')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

# Role checking functions for @user_passes_test
def admin_check(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def librarian_check(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def member_check(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views with exact names specified
@user_passes_test(admin_check, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(librarian_check, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(member_check, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')