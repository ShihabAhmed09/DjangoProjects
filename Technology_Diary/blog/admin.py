from django.contrib import admin
from .models import Post, Contact, PostComment

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Contact)
admin.site.register(PostComment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_id', 'author', 'publish_date']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['msg_id', 'name', 'email', 'subject', 'timestamp']
