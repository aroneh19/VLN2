from django.urls import path
from . import views

urlpatterns = [
    path('application.html/', views.application_form, name="Application_Form")
]