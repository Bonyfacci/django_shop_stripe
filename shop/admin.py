from django.contrib import admin

from shop.models import Item


@admin.register(Item)
class ItemListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    search_fields = ('name', 'description')
