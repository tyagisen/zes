from django.contrib import admin
from .models import Home


@admin.register(Home)
class NavigationAdmin(admin.ModelAdmin):
    list_display = ['logo']
