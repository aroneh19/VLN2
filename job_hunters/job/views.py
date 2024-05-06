from django.shortcuts import render

def job(request):
    return render(request, 'job/jobs.html')

