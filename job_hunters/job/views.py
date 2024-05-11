from django.shortcuts import render, redirect
from .models import Job, Category, Company
from user.models import User
from application.models import Application

def job(request):
    jobs = Job.objects.all()
    categories = Category.objects.all()
    companies = Company.objects.all()
    return render(request, 'job/jobs.html', {'jobs': jobs, 'categories': categories, 'companies': companies})

def filter_job_offerings(request):
    if request.method == 'GET':
        company_name = request.GET.get('company')
        category_name = request.GET.get('category')  # Get the selected category from the request
        applied_jobs = request.GET.get('checkbox')
        order_by = request.GET.get('order_by')  # Get the selected ordering from the request

        filtered_jobs = Job.objects.all() 
        if category_name:
            filtered_jobs = filtered_jobs.filter(category__name = category_name)
        if company_name:
            user = User.objects.get(first_name=company_name)
            if user:
                filtered_jobs = filtered_jobs.filter(company__user= user)
        if applied_jobs == 'on':
            logged_user = request.user
            if logged_user.is_authenticated:
                applied_jobs = Application.objects.filter(user = logged_user.id)
                filtered_jobs = filtered_jobs.exclude(application__in= applied_jobs)
        
        if order_by == 'date_offering':
            filtered_jobs = filtered_jobs.order_by('start_date')
        elif order_by == 'due_date':
            filtered_jobs = filtered_jobs.order_by('due_date')
        
        
        categories = Category.objects.all()
        companies = Company.objects.all()
        return render(request, 'job/jobs.html', {'jobs': filtered_jobs, 'categories': categories, 'companies': companies})
    else:
        # Handle other request methods, e.g., POST
        redirect('jobs')


