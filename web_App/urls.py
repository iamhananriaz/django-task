
from django.contrib import admin
from django.urls import path, include
from hello import views 
from polls import views
from blog_Web.views import custom_logout , custom_login 

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('home/', include('hello.urls')),
    path("polls/", include("polls.urls")),
    path('signup/', include('blog_Web.urls')),
    # path("", include("django.contrib.auth.urls")),
    path('login/', custom_login, name='login'),
    path('accounts/logout/',custom_logout, name='logout'),
]