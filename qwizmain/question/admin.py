from django.contrib import admin
from .models import Question




@admin.register(Question)
class QuestionRegister(admin.ModelAdmin):

    class Meta:
        ordering = ['id']

