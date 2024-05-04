from django.shortcuts import render
from django.http import JsonResponse 
from .models import User

def get_user(request):
    users = User.objects.all()
    data = [{'name': user.name, 'email': user.email} for user in users]
    return JsonResponse(data, safe=False)
