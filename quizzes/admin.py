from django.contrib import admin

from . import models


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        "correct_answer",
    ]
    autocomplete_fields = ["photos"]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "answer",
    ]
