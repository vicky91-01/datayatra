from django.contrib import admin
from .models import Question, Submisson
# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('qid', 'title', 'category', 'difficulty', 'created_at', 'updated_at')

@admin.register(Submisson)
class SubmissonAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'is_passed', 'submitted_at')