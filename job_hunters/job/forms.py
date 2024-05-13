from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'jobtype', 'location', 'category', 'start_date',
                  'date_of_offering', 'due_date', 'description']