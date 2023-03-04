from django.contrib import admin
from .models import Question,CustomUser




@admin.register(Question)
class QuestionRegister(admin.ModelAdmin):

    class Meta:
        ordering = ['id']


@admin.register(CustomUser)
class QuestionRegister(admin.ModelAdmin):

    class Meta:
        ordering = ['raiting']
