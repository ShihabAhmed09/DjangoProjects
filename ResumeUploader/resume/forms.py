from django import forms
from .models import Resume

GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

JOB_LOCATION_CHOICE = (
    ('Dhaka', 'Dhaka'),
    ('Sylhet', 'Sylhet'),
    ('Chittagong', 'Chittagong')
)


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    preferred_job_location = forms.MultipleChoiceField(choices=JOB_LOCATION_CHOICE, label='Preferred Job Location',
                                                       widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        # fields = ['name', 'date_of_birth', 'gender', 'locality', 'city', 'division', 'zip_code', 'mobile', 'email',
        #           'preferred_job_location', 'profile_pic', 'resume_file']
        fields = '__all__'
        labels = {'name': 'Full Name', 'date_of_birth': 'Date of Birth', 'zip_code': 'Zip Code',
                  'mobile': 'Mobile Number', 'email': 'Email Address', 'profile_pic': 'Profile Picture',
                  'resume_file': 'Document'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control mt-1', 'id': 'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'city': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'division': forms.Select(attrs={'class': 'form-control mt-1'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-1'}),
        }
