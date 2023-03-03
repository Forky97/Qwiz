from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings



urlpatterns = [

    path('',views.BaseHelloView.as_view(),name='home'),
    path('signin/',views.SignInView.as_view(),name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout', ),

]