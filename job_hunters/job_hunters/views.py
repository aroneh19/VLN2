from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import Profile
from company.models import Company
from job.models import Job
from random import sample, seed
from datetime import date


def random_daily_jobs(num_jobs = 4):
    date_today = date.today()
    jobs = list(Job.objects.filter(start_date__lte=date_today, due_date__gte=date_today))
    seed(str(date.today))
    sampled_jobs = sample(jobs, num_jobs)
    return sampled_jobs


def home(request):
    jobs = random_daily_jobs()
    context = {
        'jobs': jobs,
    }
    return render(request, 'index.html', context)


def handler404(request, *args, **argv):
    messages.error(request, 'The page you were looking does not exist.')
    return redirect('home')

def handler500(request, *args, **argv):
    messages.error(request, "Something bad happened, we are very sorry.")
    return redirect('home')