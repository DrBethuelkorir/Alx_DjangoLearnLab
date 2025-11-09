from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import listallbook, LibraryDetailsView, signupview  # Import your SignUpView

urlpatterns = [
    path('books/', listallbook, name='book_list'),
    path('library/<int:pk>/', LibraryDetailsView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', signupview.as_view(), name='register'),  # Add this line
]