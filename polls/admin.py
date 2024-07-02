from django.contrib import admin

# Register your models here.

from .models import Question, Choice


class ChoiceInLine(admin.ModelAdmin):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)

