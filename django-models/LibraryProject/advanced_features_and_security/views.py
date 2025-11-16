from django.shortcuts import render, redirect, get_object_or_404
from .models import Library, Book
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login 
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required  # EXACT IMPORT LINE
from django.contrib import messages

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

# Role checking functions
def admin_check(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def librarian_check(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def member_check(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(admin_check, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(librarian_check, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(member_check, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Views with custom permissions
@permission_required('relationship_app.can_add_book', login_url='/login/')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        library_id = request.POST.get('library')
        if title and author:
            library = Library.objects.get(id=library_id) if library_id else None
            Book.objects.create(title=title, author=author, library=library)
            messages.success(request, 'Book added successfully!')
            return redirect('book_list')
    libraries = Library.objects.all()
    return render(request, 'relationship_app/add_book.html', {'libraries': libraries})

@permission_required('relationship_app.can_change_book', login_url='/login/')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        library_id = request.POST.get('library')
        if library_id:
            book.library = Library.objects.get(id=library_id)
        book.save()
        messages.success(request, 'Book updated successfully!')
        return redirect('book_list')
    libraries = Library.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'libraries': libraries})

@permission_required('relationship_app.can_delete_book', login_url='/login/')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})