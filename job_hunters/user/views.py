from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User, Country, Location
from .forms import UserRegistrationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('ssn')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
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
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            
            username = form.cleaned_data['ssn']
            password = form.cleaned_data['password']

            print("Username:", username)
            print("Password:", password)


            user = authenticate(username=username, password=password)
            print("Authenticated User:", user)
            if user is not None:
                login(request, user)
                messages.info(request, 'You have successfully registered')
                messages.info(request, 'You can now login.')
                return redirect('home')
            else:
                print("Authentication failed for username:", username)
                messages.error(request, 'Authentication failed. Please check your username and password.')
        else:
            print(form.errors)
            messages.error(request, 'Registration failed!')
            messages.error(request, form.errors)
    else:
        form = UserRegistrationForm()
    
    return render(request, 'user/register.html', {'form': form, 'countries': countries, 'locations': locations})
