from django.contrib import admin

from warehouse.models import Stock, Category, Equipment


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "count",
        "stock",
    )
    list_filter = ("count",)
    search_fields = (
        "name",
        "count",
    )
