from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, profile_view, home

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),
    path('profile/', profile_view, name='profile'),
]
