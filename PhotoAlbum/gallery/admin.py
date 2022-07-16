from django.contrib import admin
from .models import Category, Photo

admin.site.register(Category)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['category', 'description', 'image']
