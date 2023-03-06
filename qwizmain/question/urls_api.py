from django.urls import path
from .views_api import AddQuestionApi,ViewApiQuestionList



urlpatterns = [


    path('api/add_question',AddQuestionApi.as_view(),name='add_question'),
    path('api/view_questions',ViewApiQuestionList.as_view(),name='view_questions'),
]