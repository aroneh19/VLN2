from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .models import Company
from .forms import CompanyRegistrationForm

def login_company(request):
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
            if user is not None:
                login(request, user)
                
            return redirect('registration_success')
        else:
            print(form.errors)
    else:
        form = CompanyRegistrationForm()
    return render(request, 'company/register.html')
