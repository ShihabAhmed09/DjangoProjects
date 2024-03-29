from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):  # User Registration form with additional email, first name, last name
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'name@example.com'}))
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):  # username and email Update form
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):  # profile_pic update form
    class Meta:
        model = Profile
        fields = ['profile_pic']
        labels = {'profile_pic': 'Profile Picture'}
