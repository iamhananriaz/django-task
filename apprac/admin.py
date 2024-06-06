from django.contrib import admin
from .models import User, Profile
from django.http import HttpResponseRedirect
from django.core import management
from django.urls import path

class UserAdmin(admin.ModelAdmin):
    change_list_template = "admin/profile_change_list.html"
    list_display = ['name', 'active']

    
class ProfileAdmin(admin.ModelAdmin):
    change_list_template = "admin/profile_change_list.html"
    list_display = ['user', 'role', 'phone_no']

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


admin.site.register(Profile, ProfileAdmin)

