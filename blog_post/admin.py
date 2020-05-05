from django.contrib import admin

# Register your models here.

from .models import UserPost

admin.site.register(UserPost)