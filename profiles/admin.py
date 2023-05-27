from django.contrib import admin
from .models import Profile


# admin.site.register(Profile)

@admin.register(Profile)
class ProfileModel(admin.ModelAdmin):
    list_filter = ('owner', 'name', 'content')
    list_display = ('owner', 'name', 'content')
