from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Category, Company
from user.models import User
from application.models import Application
from .forms import JobForm

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
        search_query = request.GET.get('search_bar')
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
        
        if search_query:
            filtered_jobs = filtered_jobs.filter(title__icontains=search_query)
        
        if order_by == 'date_offering':
            filtered_jobs = filtered_jobs.order_by('date_of_offering')
        elif order_by == 'due_date':
            filtered_jobs = filtered_jobs.order_by('due_date')
        categories = Category.objects.all()
        companies = Company.objects.all()
        return render(request, 'job/jobs.html', {'jobs': filtered_jobs, 'categories': categories, 'companies': companies})
    else:
        # Handle other request methods, e.g., POST
        redirect('jobs')

def job_info(request):
    job_id = request.GET.get('job_jid')
    job = Job.objects.get(jid = job_id)
    
    current_user = request.user.id
    application = Application.objects.filter(job=job, user=current_user).first()
    applied_date = None
    status = None
    if application:
        applied_date = application.date_applied
        status = application.status.status
    return render(request,'job/job_info.html', {'job': job, 'applied_date': applied_date, 'status': status})


@login_required
def postjob_view(request):
    user = request.user
    if request.method == 'POST':
        form = JobForm(data=request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = Company.objects.get(user=user)
            job.save()
            return redirect('company_profile')
    return render(request, "job/post-job.html")