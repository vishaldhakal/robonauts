from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('games/', views.games, name="games"),
    path('contact/', views.contact, name="contact"),
    path('send-mail/', views.send_mails, name="send_mails"),
]
