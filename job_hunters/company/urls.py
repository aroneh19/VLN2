from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='company_register'),
    path('logout/', LogoutView.as_view(template_name='company/logout.html'), name='company_logout'),
    path('profile/', views.profile_view, name='company_profile'),
    path('edit/', views.edit_view, name='edit_company'),
    path('companies/', views.companies_view, name='companies'),
    path('', views.company_view, name='company_info')
]