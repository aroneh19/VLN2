from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login.html/', LoginView.as_view(template_name='company/login.html'), name='company_login'),
    path('logout.html/', LogoutView.as_view(template_name='company/logout.html'), name='company_logout'),
    path('profile.html/', views.profile_company, name='company_profile'),
    path('register.html/', views.register_company, name='company_register'),
]