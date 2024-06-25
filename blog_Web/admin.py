from django.contrib import admin
from .models import *

admin.site.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']