from django.urls import path
from .views_api import AddQuestionApi



urlpatterns = [


    path('api/add_question',AddQuestionApi.as_view(),name='add_question')
]