from django.contrib import admin
from .models import Userdata
# Register your models here.

class Adminuserdata(admin.ModelAdmin):
    list_display=['name','email','mobileNo']

admin.site.register(Userdata,Adminuserdata)
