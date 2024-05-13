from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='user_register'),
    path('login/', views.login_view, name='user_login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='user_logout'),
    path('profile/', views.profile_view, name='user_profile'),
    path('edit/', views.edit_view, name='user_edit'),
    path('change-passsword/', views.change_password, name='change_passsword'),
    path('recomendation/', views.recomen, name= 'recomendation'),
    path('add_recomendation/', views.add_recomendation, name='add_recomendation'),
    path('experience/', views.experience, name='experience'),
    path('add_experience/', views.add_experience, name='add_experience'),
]