from django import forms
from .models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add task here...'}),
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'completed']
        labels = {'completed': 'Mark as completed'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add task here...'})
        }
