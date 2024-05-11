from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register.html/', views.register_company, name='company_register'),
    path('login.html/', views.login_view, name='company_login'),
    path('logout.html/', LogoutView.as_view(template_name='company/logout.html'), name='company_logout'),
    path('profile.html/', views.profile_company, name='company_profile'),
    path('edit.html/', views.edit_company, name='edit_company'),
    path('post_jobs.html/', views.post_jobs, name='post_jobs'),
]