from django.contrib import admin
from .models import Category, Item, Zakaz


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'alias', 'image')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'alias')


class ZakazAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'data_zakaza', 'zakaz', 'total')


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Zakaz, ZakazAdmin)



