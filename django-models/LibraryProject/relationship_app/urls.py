from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('books/', views.listallbook, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailsView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name="relationship_app/loginhtml"), name="login"),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('register/', views.register, name='register'),  # Explicitly using views.register
]