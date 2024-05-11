from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Social Security Number'
        self.fields['username'].help_text = ''

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        fields = ['phone', 'street_name', 'house_number',
                  'date_of_birth', 'picture', 'location', 'country']


