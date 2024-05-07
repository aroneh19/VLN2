from django.urls import path
from . import views

urlpatterns = [
    path('login.html/', views.login_company, name='company_login'),
    path('profile.html/', views.profile_company, name='company_profile'),
    path('register.html/', views.register_company, name='company_register'),
]