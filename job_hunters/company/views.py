from django.shortcuts import render
from .models import Company

def login(request):
    return render(request, 'company/login.html')

def profile(request):
    return render(request, 'company/profile.html')

def register(request):
    return render(request, 'company/register.html')
