from django.db import models
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-start_time']
