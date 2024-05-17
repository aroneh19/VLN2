from django.urls import path
from . import views

urlpatterns = [
    path('application/', views.application_form, name='application_form'),
    path('confirmation/', views.confirmation_page, name='confirmation_page'),
    path('submit_application/', views.submit_application, name='submit_application'),
    path('user_applications.html/', views.user_application, name="User_Applications"),
]