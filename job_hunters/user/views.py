from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User, Country, Location
from .forms import UserRegistrationForm

def login_user(request):
    if request.method == "POST":
        ssn = request.POST.get('ssn')
        password = request.POST.get('password')

        user = authenticate(request, ssn=ssn, password=password)

        if user is not None:
            return redirect('home')

    return render(request, 'user/login.html')

def edit_user(request):
    return render(request, 'user/edit.html')

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
            form.save()
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'user/register.html', {'form': form, 'countries': countries, 'locations': locations})
