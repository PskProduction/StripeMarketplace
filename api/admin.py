from django.contrib import admin

from api.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
        'price',
    ]

    search_fields = ["name"]
