from django.contrib import admin
from .models import *
from django.http import HttpResponseRedirect
from django.core import management
from django.urls import path


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

class PhoneNumberFilter(admin.SimpleListFilter):
    title = 'Phone Number'
    parameter_name = 'phone_no'

    def lookups(self, request, model_admin):
        return (
            ('+9230', '+9230'),
            ('+9231', '+9231'),
            ('+9232', '+9232'),
            ('+9233', '+9233'),
            ('+9234', '+9234'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(phone_no__startswith=value)
        

admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list.html"
    list_display = ['user', 'email', 'phone_number']

    def fake_data(self, request):
       success = management.call_command("fake_user_profile")
       return HttpResponseRedirect("../")
      
    def get_urls(self):
       urls = super().get_urls()
       custom_urls = [
           path(
               "fake_data/",
               self.fake_data,
               name = 'fake_data'
           )
       ]
       return custom_urls + urls