from django.urls import path
from . import views

urlpatterns = [
    path('register.html/', views.register, name='user_register'),
    path('login.html/', views.login, name='user_login'),
    
]