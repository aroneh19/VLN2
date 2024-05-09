from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register.html/', views.register_user, name='user_register'),
    path('login.html/', LoginView.as_view(template_name='user/login.html'), name='user_login'),
    path('logout.html/', LogoutView.as_view(template_name='user/logout.html'), name='user_logout'),
    path('edit.html/', views.edit_user, name='user_edit'),
    path('profile.html/', views.profile_user, name='user_profile'),
]