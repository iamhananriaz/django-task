from django.urls import path
from . import views
from django.urls import path
from django.conf.urls import handler404
from django.shortcuts import render
from django.contrib import admin
app_name = "hello"

urlpatterns = [
    path('registration/', views.showformdata , name = "dealerurl"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

handler404 = 'hello.urls.custom_404_view'
