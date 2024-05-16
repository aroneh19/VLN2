from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='user_register'),
    path('login/', views.login_view, name='user_login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='user_logout'),
    path('profile/', views.profile_view, name='user_profile'),
    path('edit/', views.edit_view, name='user_edit'),
    path('change-passsword/', views.change_password, name='change_password'),
    path('recommendation/', views.recommen, name= 'recommendation'),
    path('add_recommendation/', views.add_recommendation, name='add_recommendation'),
    path('experience/', views.experience, name='experience'),
    path('add_experience/', views.add_experience, name='add_experience'),
    path('delete/experience/<int:eid>/', views.delete_experience, name='delete_experience'),
    path('delete/recommendation/<int:rid>/', views.delete_recommendation, name='delete_recommendation')
]