from django.shortcuts import render
from .models import Application

# Create your views here.
def application_form(request):
    return render(request, 'application/application.html')