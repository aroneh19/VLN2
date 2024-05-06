from django.shortcuts import render, redirect
from django.http import JsonResponse 
from .models import User, Country, Location
from .forms import UserRegistrationForm
import os
from django.contrib.auth.hashers import make_password

def register(request):
    countries = Country.objects.all()
    postcodes = Location.objects.all()
    return render(request, 'user/register.html', {'countries': countries, 'postcodes': postcodes})

def login(request):
    return render(request, 'user/login.html')

def edit(request):
    return render(request, 'user/edit.html')

def profile(request):
    return render(request, 'user/profile.html')

def save_user_with_hashed_password(user_data):
    # Hash the password before saving
    hashed_password = make_password(user_data['password'])
    user_data['password'] = hashed_password

    user = User(**user_data)
    user.save()

def register_user(request):
    countries = Country.objects.all()
    postcodes = Location.objects.all()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form, 'countries': countries, 'postcodes': postcodes})
