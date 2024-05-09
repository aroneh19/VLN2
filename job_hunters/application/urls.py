from django.urls import path
from . import views

urlpatterns = [
    path('application.html/', views.application_form, name="Application_Form"),
    path('user_applications.html/', views.user_application, name="User_Applications"),
    path('submit_application.html/', views.submit_application, name="submit_application"),
]