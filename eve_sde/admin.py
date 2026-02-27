"""Admin models"""

# Django
from django.contrib import admin

from . import models

# Register your models here.
# admin.site.register(models.ItemCategory)
# admin.site.register(models.ItemGroup)
# admin.site.register(models.ItemType)


@admin.register(models.SolarSystem)
class SystemAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_region', 'get_constellation']
    search_fields = [
        'name',
        'constellation__region__name',
        'constellation__name'
    ]

    def get_region(self, obj):
        return obj.constellation.region.name

    def get_constellation(self, obj):
        return obj.constellation.name

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('constellation', 'constellation__region')

    # def get_model_perms(self, request):
    #     return {}


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    # def get_model_perms(self, request):
    #     return {}


@admin.register(models.Constellation)
class ConstellationAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_region']
    search_fields = ['name', 'region__name']

    def get_region(self, obj):
        return obj.region.name

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('region')

    # def get_model_perms(self, request):
    #     return {}


@admin.register(models.Moon)
class MoonAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_region', 'get_constellation', 'get_system']
    search_fields = [
        'name',
        'system__constellation__region__name',
        'system__constellation__name',
        'system__name'
    ]

    def get_region(self, obj):
        return obj.system.constellation.region.name

    def get_constellation(self, obj):
        return obj.system.constellation.name

    def get_system(self, obj):
        return obj.system.name

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('system__constellation__region', 'system__constellation', 'system')

    # def get_model_perms(self, request):
    #     return {}


@admin.register(models.Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_region', 'get_constellation', 'get_system']
    search_fields = [
        'name',
        'system__constellation__region__name',
        'system__constellation__name',
        'system__name'
    ]

    def get_region(self, obj):
        return obj.system.constellation.region.name

    def get_constellation(self, obj):
        return obj.system.constellation.name

    def get_system(self, obj):
        return obj.system.name

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('system__constellation__region', 'system__constellation', 'system')

    # def get_model_perms(self, request):
    #     return {}
