from django.contrib import admin
from .models import Category, Item, Zakaz, Annotation, Currency, ItemForeign


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'alias', 'image')
    actions = ['set_group']

    def set_group(modeladmin, request, queryset):
        itemforeign = []
        queryset = Item.objects.all()
        for object in queryset:
            i_f = ItemForeign(name = object.name, price = object.price, description = object.description,
                              alias = object.alias, image = object.image, category = object.category,
                              currency = Currency.objects.get(name='Доллар'))
            itemforeign.append(i_f)

        ItemForeign.objects.bulk_create(itemforeign)
    set_group.short_description = 'Перенести в группу Товары_импорт'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'alias')


class ZakazAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'data_zakaza', 'zakaz', 'total')


class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created_date', 'item_annot')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate')


class ItemForeignAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rate', 'cost', 'category', 'alias', 'image')
    fields = ('name', 'price', 'description', 'category', 'alias', 'image', 'currency')
    actions = ['update_model']

    def update_model(modeladmin, request, queryset):
        for object in queryset:
            object.save()
    update_model.short_description = 'Обновить цены'


admin.site.register(Annotation, AnnotationAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Zakaz, ZakazAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ItemForeign, ItemForeignAdmin)



