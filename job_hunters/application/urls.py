from django.urls import path
from . import views

urlpatterns = [
    path('application/', views.application_form, name='application_form'),
    path('confirmation/', views.confirmation_page, name='confirmation_page'),
    path('user_applications.html/', views.user_application, name="User_Applications"),
    path('submit_review/', views.submit_review, name="submit_review"),
    path('review/', views.review, name='review'),
]