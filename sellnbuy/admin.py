from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
from .models import Product, Profile, Message


# Define an inline admin descriptor for profile model
# which acts a bit like a singleton

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'

# Define a new User admin

# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)

# Register your models here.

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

admin.site.register(Product)
# admin.site.register(Profile, UserAdmin)
admin.site.register(Profile)
admin.site.register(Message)



