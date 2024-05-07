from django.shortcuts import render
from .models import Application
from user.models import Recommendation, Experience, Country, User


def application_form(request):
    user_id = 3
    user = User.objects.get(uid=user_id)
    recommendations = Recommendation.objects.filter(user=user)
    experiences = Experience.objects.filter(user=user)
    countries = Country.objects.all()
    return render(request, 'application/application.html', {'recommendations': recommendations, 'experiences': experiences, 'countries': countries, 'user': user})

def user_application(request):
    
    return render(request, 'application/user_application.html')

