from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['ssn', 'name', 'password', 'phone', 'email', 'street_name', 
                  'house_number', 'date_of_birth', 'picture', 'location', 'country']