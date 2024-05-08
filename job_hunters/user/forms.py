from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['ssn', 'name', 'password', 'phone', 'email', 'street_name', 
                  'house_number', 'date_of_birth', 'picture', 'location', 'country']
        
class CustomAuthenticationForm(AuthenticationForm):
    ssn = forms.CharField(label="Social Security Number", max_length=11)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = self.fields.pop('ssn')