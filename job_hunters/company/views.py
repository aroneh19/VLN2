from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from .models import Company
from .forms import CompanyRegistrationForm

def login_company(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            goto = request.GET.get('next') or 'profile'
            return redirect(goto)
        else:
            messages.error(request, 'Login failed!')
            messages.error(request, form.errors)
    return render(request, 'company/login.html')

def profile_company(request):
    return render(request, 'company/profile.html')

def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
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
    return render(request, 'company/register.html')
