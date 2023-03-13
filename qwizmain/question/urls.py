from django.urls import path
from . import views,views_websocket
from django.contrib.auth.views import LogoutView
from django.conf import settings



urlpatterns = [

    path('',views.BaseHelloView.as_view(),name='home'),
    path('game/',views.QuestionDetailView.as_view(),name='game'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('signin/',views.SignInView.as_view(),name='signin'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('contact/success',views.Success,name='success'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout', ),
    path('game/top10',views.Top10.as_view(),name='top10'),
    path('chat/',views_websocket.ChatView.as_view(),name='chat'),
    path("chat/<str:room_name>/", views_websocket.RoomView.as_view(), name="room"),

]