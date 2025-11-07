from django.urls import path
from .views import list_book, LibraryDetailView  # Correct function and class names

urlpatterns = [
    path('books/', listallbook, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]