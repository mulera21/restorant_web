from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "image", "status")
    list_filters = ("status",)
    search_field = ("meal", "description")


admin.site.register(Item, MenuItemAdmin)