from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'option_1': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'option_2': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'option_3': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'option_4': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'answer': forms.TextInput(attrs={'class': 'form-control mt-1'}),
        }
