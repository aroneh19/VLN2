from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Category, Company
from application.models import Status
from user.models import User
from application.models import Application
from .forms import JobForm
from django.http import HttpResponse
from datetime import date

def job(request):
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
        # Handle other request methods, e.g., POST
        redirect('jobs')

def job_info(request, applied_date=None, status=None):
    job_id = request.GET.get('job_jid')
    job = Job.objects.get(jid = job_id)
    
    current_user = request.user.id
    application = Application.objects.filter(job=job, user=current_user).first()
    if application:
        applied_date = application.date_applied
        status = application.status.status
    context = {
        'job': job,
        'applied_date': applied_date,
        'status': status
    }
    return render(request,'job/job_info.html', context)

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
    return render(request, "job/post-job.html", {'form': JobForm()})

def company_listings(request):
    curr_user = request.user
    curr_company = Company.objects.get(user_id = curr_user.id)   
    jobs = Job.objects.filter(company = curr_company)
    
    
    return render(request, 'company/company_listings.html', {'jobs': jobs})

def job_applicants(request):
    job_id = request.GET.get('job_jid')
    return renderJobApplicants(request,job_id)    
        
def renderJobApplicants(request, job_id):    
    curr_job = Job.objects.get(jid = job_id)
    applicants = Application.objects.filter(job = curr_job)
    for applicant in applicants:
        applicant.user.profile.age = calculate_age(applicant.user.profile.date_of_birth)    
    return render(request, 'company/job_applicants.html', {'applicants' :applicants}) 

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def status_response(request):
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

        return renderJobApplicants(request,job_id)
        #return HttpResponse('Success: Application status updated')  # Return success message
