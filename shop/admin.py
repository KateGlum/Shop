from django.contrib import admin
from .models import Category, Item, Zakaz, Annotation


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'alias', 'image')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'alias')


class ZakazAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'data_zakaza', 'zakaz', 'total')


class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created_date', 'item_annot')


admin.site.register(Annotation, AnnotationAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Zakaz, ZakazAdmin)



