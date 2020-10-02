from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogs_list,name="blogs_list"),
    path('<str:slug>/',views.blog_single,name="blog_single"),
]
