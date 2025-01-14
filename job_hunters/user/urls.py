from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('comp_or_login/', views.c_or_u_login, name='c_or_u_login'),
    path('comp_or_user_signup/', views.c_or_u_signup, name='c_or_u_signup'),
    path('register/', views.register_view, name='user_register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='user_logout'),
    path('profile/', views.profile_view, name='user_profile'),
    path('edit/', views.edit_view, name='user_edit'),
    path('change-passsword/', views.change_password, name='change_password'),
    path('add_recommendation/', views.add_recommendation, name='add_recommendation'),
    path('add_experience/', views.add_experience, name='add_experience'),
    path('delete/experience/<int:eid>/', views.delete_experience, name='delete_experience'),
    path('delete/recommendation/<int:rid>/', views.delete_recommendation, name='delete_recommendation')
]