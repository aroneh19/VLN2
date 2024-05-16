from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company

class CustomCompanyCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Company Name'
    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password1", "password2")
        
class EditProfile(forms.ModelForm):
    class Meta:
        model = Company    
        fields = ['address', 'logo', 'cover',
                'description', 'website']