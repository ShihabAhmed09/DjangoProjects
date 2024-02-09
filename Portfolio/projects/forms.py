from django import forms
from .models import Project
from ckeditor.widgets import CKEditorWidget


class ProjectForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Project
        fields = ['title', 'content', 'thumbnail', 'active', 'featured', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),
        }
