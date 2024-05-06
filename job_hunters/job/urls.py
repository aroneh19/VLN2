from django.urls import path
from . import views

urlpatterns = [
    path('jobs.html/', views.job, name='jobs'),
]