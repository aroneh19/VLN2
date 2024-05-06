from django.urls import path
from . import views

urlpatterns = [
    path('login.html/', views.login, name='company_login'),
    path('profile.html/', views.profile, name='company_profile'),
    path('register.html/', views.register, name='company_register'),
]