from django.contrib import admin
from .models import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import management
from django_object_actions import DjangoObjectActions, action
from django.urls import path


    
class ProfileAdmin(admin.ModelAdmin):
    change_list_template = "admin/profile_change_list.html"
    list_display = ['user', 'role', 'phone_no']

    def fake_data(self, request):
       print("1st")
       success = management.call_command("fake_users")
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

class UserAdmin(admin.ModelAdmin):
   list_display = ["name", "active"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdmin)


class infoAdmin(DjangoObjectActions, admin.ModelAdmin):

    def change_about(self, request, obj):
        if not obj.about:
            obj.about="Who are you?"
        else: 
            obj.about=""
        obj.save()

    change_actions = ("change_about",)


admin.site.register(info, infoAdmin)