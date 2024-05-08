from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User, Country, Location
from .forms import UserRegistrationForm, CustomAuthenticationForm

def login_user(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            goto = request.GET.get('next') or 'profile'
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, 'Login failed!')
            messages.error(request, form.errors)
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
            login(request, user)
            messages.info(request, 'You have successfully registered')
            messages.info(request, 'You can now login.')
            return redirect('home')                
        else:
            messages.error(request, 'Registration failed!')
            messages.error(request, form.errors)
    
    return render(request, 'user/register.html', {'form': form, 'countries': countries, 'locations': locations})
