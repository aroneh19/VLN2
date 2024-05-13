from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm as BaseUserChangeForm
from django.contrib.auth.models import User
from .models import Profile, Recommendation, Experience

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

class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        fields = ['phone', 'country', 'location', 'street_name', 'house_number', 'picture']

class RecomendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['name', 'email', 'phone_number', 'role', 'may_be_contacted']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['place_of_work', 'role', 'start_date', 'end_date']



