from django.urls import path
from . import views

urlpatterns = [
    path('register.html/', views.register_user, name='user_register'),
    path('login.html/', views.login_user, name='user_login'),
    path('edit.html/', views.edit_user, name='user_edit'),
    path('profile.html/', views.profile_user, name='user_profile'),
]