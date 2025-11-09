from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.listallbook, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailsView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name="relationship_app/loginhtml"), name="login"),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('register/', views.register.as_view(), name='register'),
    
    # Role-based URL patterns as specified
    path('admin/dashboard/', views.admin_view, name='admin_view'),
    path('librarian/dashboard/', views.librarian_view, name='librarian_view'),
    path('member/dashboard/', views.member_view, name='member_view'),
]