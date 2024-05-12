from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register.html/', views.register_view, name='user_register'),
    path('login.html/', views.login_view, name='user_login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='user_logout'),
    path('edit.html/', views.edit_view, name='user_edit'),
    path('profile.html/', views.profile_view, name='user_profile'),
    path('change_passsword.html/', views.password_change, name='change_passsword'),
]