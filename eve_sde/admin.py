"""Admin models"""

# Django
from django.contrib import admin

# Django EVE SDE
from eve_sde.models.types import ItemType


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
