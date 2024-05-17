from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm as BaseUserChangeForm
from django.contrib.auth.models import User
from .models import Profile, Recommendation, Experience

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Type in email',
            'class': 'form-control'
        })
    )
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Type in first name',
            'class': 'form-control'
        })
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Type in last name',
            'class': 'form-control'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Type in username',
            'class': 'form-control'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type in password',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type in password',
            'class': 'form-control'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Type in username', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Type in password', 'class': 'form-control'})
    )

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].help_text = ''

#     class Meta:
#         model = User
#         fields = ("username", "first_name", "last_name", "email", "password1", "password2")

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
        fields = ['phone', 'date_of_birth', 'country', 'location', 'street_name', 'house_number', 'picture']

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['name', 'email', 'phone_number', 'role', 'may_be_contacted']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['place_of_work', 'role', 'start_date', 'end_date']



