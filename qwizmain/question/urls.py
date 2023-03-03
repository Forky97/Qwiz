from django.urls import path
import views



urlpatterns = [

    path('home/',views.BaseHelloView.as_view,name='home')


]