from django.contrib import admin
from .models import Resume


# Register your models here.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'gender', 'locality', 'city', 'division', 'zip_code', 'mobile', 'email',
                    'preferred_job_location', 'profile_pic', 'resume_file']
