from django.shortcuts import render, redirect
from django.contrib import messages

def jobs():
    # Sækja störf sem henta á home page
    pass


def index(request):
    return render(request, 'index.html')


def handler404(request, *args, **argv):
    messages.error(request, 'The page you were looking does not exist.')
    return redirect('home')

def handler500(request, *args, **argv):
    messages.error(request, "Something bad happened, we are very sorry.")
    return redirect('home')