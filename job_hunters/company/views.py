from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Company
from  .forms import CustomCompanyCreationForm

def login_company(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login failed!')
            messages.error(request, form.errors)
    return render(request, 'company/login.html')

def profile_company(request):
    return render(request, 'company/profile.html')

def register_company(request):
    if request.method == 'POST':
        form = CustomCompanyCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            company = Company.objects.create(user=user, name=user.first_name)
            return redirect('user_login')
        else:
            print(form.errors)
    else:
        form = CustomCompanyCreationForm()
    
    
    return render(request, 'user/register.html', {'form': form})


@login_required
def company_view(request):
    return render(request, "company/profile.html")

@login_required
def edit_comapny(request):
    return render(request, "company/edit.html")