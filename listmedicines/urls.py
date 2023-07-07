from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path('home',views.home,name="home"),
   path('list-medicines',views.list_medicines,name="list_medicines"),
]