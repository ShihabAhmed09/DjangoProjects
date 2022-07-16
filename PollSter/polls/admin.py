from django.contrib import admin
from .models import Question, Choice


# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Welcome to the Pollster Admin Area'


# Show choices with Question combining Choice model with Question model
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # how many extra fields we want


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
