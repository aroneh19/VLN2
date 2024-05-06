from django.shortcuts import render
from .models import Application

# Create your views here.
def application_form(request):
    return render(request, 'application/application.html')

def user_application(request):
    return render(request, 'application/user_application.html')