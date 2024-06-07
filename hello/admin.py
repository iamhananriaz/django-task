from django.contrib import admin
from .models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import management
from django.urls import path
from django_object_actions import DjangoObjectActions, action



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_cat', 'publish_date' ,'user']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'sung_by']
    
@admin.register(ExamCenter)
class ExamcenterAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'center_name', 'city']

@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'center_name', 'city']
    ordering = ['id']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email' ,'address']

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ['name', 'niche', 'sale']

@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    model = Quality

    fiels = ['quality', 'is_good']
    list_display = ['quality', 'is_good']
    actions = ['make_bad']
    def make_bad(self, request, queryset):
        queryset.update(is_good = False)


        








    
    