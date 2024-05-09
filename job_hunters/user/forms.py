from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Profile

class ProfileRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Social Security Number', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profile
        fields = ['phone', 'street_name', 'house_number', 'date_of_birth', 'picture', 'location', 'country']


