from django.urls import path
from . import views
from django.urls import path
from django.conf.urls import handler404
from django.shortcuts import render
from django.contrib import admin
app_name = "hello"


from .views import signup, home , blog

urlpatterns = [

    path('', home, name='home'),

]