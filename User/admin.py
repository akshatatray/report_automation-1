from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
#
# class UserAdmin
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = {'name' , 'email' ,'phone_no' , 'profile_picture'}
admin.site.register(User)
