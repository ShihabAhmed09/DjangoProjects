from django.contrib import admin
from .models import Task


# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_time', 'completed']
