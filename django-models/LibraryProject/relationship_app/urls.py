from django.urls import path
from . import views


urlpatterns =[
    path('books/',views.listallbook),
    path('library/', views.Librarydetails.as_view())
]