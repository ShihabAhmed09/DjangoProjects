from django import forms
from .models import BookList


class BookForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields = '__all__'
        labels = {'name': 'Book Name'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Enter Book Name'}),
            'author': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Enter Author Name'}),
            'publication': forms.TextInput(
                attrs={'class': 'form-control mt-1', 'placeholder': 'Publisher of the book'}),
            'category': forms.Select(attrs={'class': 'form-control mt-1'})
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select Book Category"
