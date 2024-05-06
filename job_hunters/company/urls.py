from django.urls import path
from . import views

urlpatterns = [
    path('register.html/', views.register, name='company_register'),
    path('login.html/', views.login, name='company_login'),
]