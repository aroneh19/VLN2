from django import forms
from .models import Company

class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['ssn', 'name', 'password', 'address',
                  'logo', 'cover', 'description', 'website']