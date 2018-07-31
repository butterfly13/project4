from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Profile, Message, State

# Register your models here.
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(State)


