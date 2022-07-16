from django.db import models

DIVISION_CHOICE = (
    ('Dhaka', 'Dhaka'),
    ('Chittagong', 'Chittagong'),
    ('Sylhet', 'Sylhet'),
    ('Rajshahi', 'Rajshahi'),
    ('Khulna', 'Khulna'),
    ('Barisal', 'Barisal'),
    ('Rangpur', 'Rangpur'),
    ('Mymenshing', 'Mymenshing'),
)


class Resume(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    division = models.CharField(choices=DIVISION_CHOICE, max_length=100)
    zip_code = models.CharField(max_length=20)
    mobile = models.CharField(max_length=100)
    email = models.EmailField()
    preferred_job_location = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='resume/profile_pics')
    resume_file = models.FileField(upload_to='resume/docs')

    class Meta:
        ordering = ['name']
