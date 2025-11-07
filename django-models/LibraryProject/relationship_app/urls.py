from django.urls import path
from .views import list_books,LibrarydetailsView


urlpatterns =[
    path('books/',views.listallbook),
    path('library/', views.LibrarydetailsView.as_view())
]