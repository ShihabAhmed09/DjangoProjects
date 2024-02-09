from django.contrib import admin
from .models import Category, BookList

admin.site.register(Category)


@admin.register(BookList)
class BookListAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'category', 'publication']
