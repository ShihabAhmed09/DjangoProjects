from django import forms
from .models import JobPost, Candidates


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = '__all__'
        exclude = ['name', 'posted']


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = '__all__'
        labels = {'dob': 'Date of Birth'}
        exclude = ['company', 'position', 'applied']
        widgets = {'dob': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'})}
