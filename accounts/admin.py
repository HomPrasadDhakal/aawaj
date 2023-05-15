from django.contrib import admin
from accounts.models import User, Profile
from django.utils.html import format_html
from django.contrib.auth.models import Group



admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name","user_type", "is_active")
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "address", "main_profile_picture")

    def main_profile_picture(slef, obj):
        return format_html('<img src="{0}" width="auto" height="50px">'.format(obj.profile_picture.url))
