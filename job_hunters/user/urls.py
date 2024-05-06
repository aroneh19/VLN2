from django.urls import path
from . import views

urlpatterns = [
    path('register.html/', views.register_user, name='user_register'),
    path('login.html/', views.login, name='user_login'),
    path('edit.html/', views.edit, name='user_edit'),
    
]