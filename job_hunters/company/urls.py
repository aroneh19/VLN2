from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_company, name='company_register'),
    path('login/', views.login_view, name='company_login'),
    path('logout/', LogoutView.as_view(template_name='company/logout.html'), name='company_logout'),
    path('profile/', views.profile_company, name='company_profile'),
    path('edit/', views.edit_company, name='edit_company'),
    path('post-jobs/', views.post_jobs, name='post_jobs'),
]