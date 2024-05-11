from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register.html/', views.register_user, name='user_register'),
    path('login.html/', views.login_view, name='user_login'),
    #path('login.html/', LoginView.as_view(template_name='user/login.html'), name='user_login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='user_logout'),
    path('edit.html/', views.edit_user, name='user_edit'),
    path('profile.html/', views.profile_view, name='user_profile'),
]