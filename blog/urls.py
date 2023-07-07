from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
#    path('/home',views.home,name="home"),
   path('blog',views.blog,name="blog"),
   path('blog/posts/<str:pk>',views.posts,name='posts'),
]