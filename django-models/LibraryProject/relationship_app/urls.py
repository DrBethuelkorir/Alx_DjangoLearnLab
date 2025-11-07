from django.urls import path
from .views import list_books,LibraryDetailsView


urlpatterns =[
    path('books/',views.listallbook),
    path('library/', views.LibraryDetailsView.as_view())
]