from django.contrib import admin

# Register your models here.
from .models import *


class ImageInUserInline(admin.TabularInline):
    model = User_photo
    extra = 0




admin.site.register(User_M)
admin.site.register(User_photo)
admin.site.register(Message)
admin.site.register(Chat)