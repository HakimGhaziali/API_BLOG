from django.contrib import admin
from django.urls import path , include
from .views import PostSerial , PostDetailSerial , UserlSerial , UserDetaillSerial


urlpatterns = [
    path('', PostSerial.as_view() , name = 'post_serial'),
    path('<int:pk>', PostDetailSerial.as_view() , name = 'postdetail_serial'),
    path('user', UserlSerial.as_view() , name = 'user_serial'),
    path('user/<int:pk>', UserDetaillSerial.as_view() , name = 'userdetail_serial'),

]