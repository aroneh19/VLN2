from django.shortcuts import render
from .models import Job

def job(request):
    jobs = Job.objects.all()
    return render(request, 'job/jobs.html', {'jobs': jobs})

