from django.shortcuts import render
from django.http import JsonResponse 
from .models import User, Country, Location
import os

def register(request):
    countries = Country.objects.all()
    postcodes = Location.objects.all()
    return render(request, 'user/register.html', {'countries': countries, 'postcodes': postcodes})
