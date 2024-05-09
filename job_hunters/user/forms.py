from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Profile

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'street_name', 'house_number', 'date_of_birth', 'picture', 'location', 'country']
