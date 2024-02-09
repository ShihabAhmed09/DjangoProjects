from django.contrib import admin
from .models import Skill, Contact, Certificate, Category, Post, PostComment, Tag, Project

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(PostComment)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'knowledge', 'created']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'organization']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'created', 'is_read']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'active', 'featured']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'active', 'featured']
