from django.urls import path
from . import views
from django.urls import path
from django.contrib import admin
app_name = "hello"

urlpatterns = [
    path('registration/', views.showformdata , name = "dealerurl"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]