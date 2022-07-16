from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class JobPost(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    experience = models.IntegerField(null=True)
    location = models.CharField(max_length=2000, null=True)
    posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-posted']


class Candidates(models.Model):
    GENDER = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other'),
    )
    name = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)
    mobile = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    resume = models.FileField(null=True)
    position = models.CharField(max_length=255, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    applied = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-applied']
