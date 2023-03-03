from django.urls import path
from . import views



urlpatterns = [

    path('',views.BaseHelloView.as_view(),name='home')


]