from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .models import User, Country, Location
from .forms import UserRegistrationForm
import os


def login_user(request):
    return render(request, 'user/login.html')

def edit_user(request):
    user_id = 3
    user = User.objects.get(uid=user_id)
    return render(request, 'user/edit.html', {'user': user})

def profile_user(request):
    user_id = 3
    user = User.objects.get(uid=user_id)
    return render(request, 'user/profile.html', {'user': user})

def register_user(request):
    countries = Country.objects.all()
    locations = Location.objects.all()
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            
            ssn = form.cleaned_data['ssn']
            password = form.cleaned_data['password']
            user = authenticate(request, username=ssn, password=password)
            if user is not None:
                login(request, user)
                
            return redirect('registration_success')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    
    return render(request, 'user/register.html', {'form': form, 'countries': countries, 'locations': locations})

