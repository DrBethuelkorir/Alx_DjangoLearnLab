from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import listallbook, LibraryDetailsView, SignUpView  # Make sure SignUpView is imported

urlpatterns = [
    path('books/', listallbook, name='book_list'),
    path('library/<int:pk>/', LibraryDetailsView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name="relationship_app/loginhtml"), name="login"),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # Added template
    path('register/', SignUpView.as_view(), name='register'),  # Register path
]