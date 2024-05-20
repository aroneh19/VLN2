from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Category, Company
from application.models import Status
from user.models import User
from application.models import Application
from .forms import JobForm
from django.http import HttpResponse
from datetime import date
from django.utils import timezone
from django.contrib import messages

def job(request):
    """Renders the job listings page with filtering options.

    Args:
    - request: HTTP request object.

    Returns:
    - Rendered HTTP response displaying job listings.
    """
    current_date = date.today()
    jobs = Job.objects.filter(due_date__gte=current_date)
    categories = Category.objects.all()
    companies = Company.objects.all()
    context = {
        'jobs': jobs,
        'categories': categories,
        'companies': companies
    }
    return render(request, 'job/jobs.html', context)

def filter_job_offerings(request):
    """Renders the job listings page with filtering options.

    Args:
    - request: HTTP request object.

    Returns:
    - Rendered HTTP response displaying job listings.
    """
    if request.method == 'GET':
        company_name = request.GET.get('company')
        category_name = request.GET.get('category')  # Get the selected category from the request
        applied_jobs = request.GET.get('checkbox')
        order_by = request.GET.get('order_by')  # Get the selected ordering from the request
        search_query = request.GET.get('search_bar')
        
        current_date = date.today()
        filtered_jobs = Job.objects.filter(due_date__gte=current_date)
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
                filtered_jobs = filtered_jobs.filter(application__in= applied_jobs)
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
        redirect('jobs')

def job_info(request, applied_date=None, status=None, is_company=False):
    """Displays detailed information about a job including application status.

    Args:
    - request: HTTP request object.
    - applied_date (optional): Date when the user applied for the job.
    - status (optional): Application status.
    - is_company (optional): Boolean indicating if the user is a company.

    Returns:
    - Rendered HTTP response displaying job details.
    """
    job_id = request.GET.get('job_jid')
    job = Job.objects.get(jid = job_id)
    
    current_user = request.user.id
    if current_user:
        is_company = Company.objects.filter(user=request.user).exists()
    application = Application.objects.filter(job=job, user=current_user).first()
    if application:
        applied_date = application.date_applied
        status = application.status.status
    
    current_date = timezone.now().date()

    context = {
        'job': job,
        'applied_date': applied_date,
        'status': status,
        'is_company': is_company,
        'current_date': current_date,
    }
    return render(request,'job/job_info.html', context)

@login_required
def postjob_view(request):
    """Handles posting a new job by a logged-in user.

    Args:
    - request: HTTP request object.

    Returns:
    - Rendered HTTP response for posting a job.
    """
    user = request.user
    if request.method == 'POST':
        form = JobForm(data=request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = Company.objects.get(user=user)
            job.save()
            messages.success(request, 'Job posted successfully.')
            return redirect('company_profile')
        else:
            messages.error(request, 'Failed to post job. Please correct the errors below.')
    return render(request, "job/post-job.html", {'form': JobForm()})

def company_listings(request):
    """Displays job listings for the current company.

    Args:
    - request: HTTP request object.

    Returns:
    - Rendered HTTP response displaying job listings for the company.
    """
    curr_user = request.user
    curr_company = Company.objects.get(user_id = curr_user.id)   
    jobs = Job.objects.filter(company = curr_company)
    return render(request, 'company/company_listings.html', {'jobs': jobs})

def job_applicants(request):
    """Displays job applicants for a particular job.

    Returns:
    - Rendered HTTP response displaying job applicants.
    """
    job_id = request.GET.get('job_jid')
    return renderJobApplicants(request,job_id)    
        
def renderJobApplicants(request, job_id):
    """
    Renders job applicants for a particular job.

    Args:
    - job_id: ID of the job.

    Returns:
    - Rendered HTTP response displaying job applicants.
    """    
    curr_job = Job.objects.get(jid = job_id)
    applicants = Application.objects.filter(job = curr_job)
    for applicant in applicants:
        applicant.user.profile.age = calculate_age(applicant.user.profile.date_of_birth)    
    return render(request, 'company/job_applicants.html', {'applicants' :applicants}) 

def calculate_age(born):
    """
    Calculates age based on the provided date of birth.

    Args:
    - born: Date of birth (datetime object).

    Returns:
    - Age in years (integer).
    """
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def status_response(request):
    """Handles accepting or rejecting job applications.

    Returns:
    - Rendered HTTP response displaying updated job applicants.
    """
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        job_id = request.POST.get('job_id')
        action = request.POST.get('action')
        try:
            application = Application.objects.get(aid=application_id)
            
        except:
            return HttpResponse('Error: Application not found', status=400)  # Return error message with status code 400
        if action == 'accept':
            application.status = Status.objects.get(sid=1)
        elif action == 'reject':
            application.status = Status.objects.get(sid=3)
        application.save()
        messages.success(request, 'Application status updated successfully.')
        return renderJobApplicants(request,job_id)