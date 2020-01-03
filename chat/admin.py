from django.contrib import admin

# Register your models here.
from .models import *


class ImageInUserInline(admin.TabularInline):
    model = User_photo
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User_M._meta.fields]
    inlines = [ImageInUserInline]

    class Meta:
        model = User_M


admin.site.register(User_M, UserAdmin)
admin.site.register(User_photo)
admin.site.register(Message)
admin.site.register(Chat)