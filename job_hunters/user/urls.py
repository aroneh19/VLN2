from django.urls import path
from . import views

urlpatterns = [
    path('edit.html/', views.edit, name='user_edit'),
    path('login.html/', views.login, name='user_login'),
    path('register.html/', views.register, name='user_register'),
    path('profile.html/', views.profile, name='user_profile'),
]