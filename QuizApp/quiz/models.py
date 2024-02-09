from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    question = models.CharField(max_length=500, null=True)
    option_1 = models.CharField(max_length=255, null=True)
    option_2 = models.CharField(max_length=255, null=True)
    option_3 = models.CharField(max_length=255, null=True)
    option_4 = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.question


class Attempt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attempt = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    percentage = models.FloatField()
    correct = models.IntegerField()
    incorrect = models.IntegerField()
    total = models.IntegerField()
    time_taken = models.CharField(null=True, max_length=100)
    created = models.DateTimeField(null=True, default=timezone.now)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        ordering = ['-created']
