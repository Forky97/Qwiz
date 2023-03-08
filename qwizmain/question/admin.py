from django.contrib import admin
from .models import Question,CustomUser
from rest_framework.authtoken.models import Token





@admin.register(Question)
class QuestionRegister(admin.ModelAdmin):

    class Meta:
        ordering = ['id']


@admin.register(CustomUser)
class QuestionRegister(admin.ModelAdmin):

    class Meta:
        ordering = ['raiting']


@admin.register(Token)
class QuestionRegister(admin.ModelAdmin):
    pass
