from django.contrib import admin

from restShop.models import Product, Type, Price


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'quantity', 'barcode', 'dateUpdate', 'type', ]
    list_editable = [ 'price', 'quantity', 'barcode', 'type' ]
    list_filter = ['type']
    search_fields = ['name']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    model = Type
    list_display = ['name', 'characteristics', ]
    list_editable = ['characteristics', ]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    model = Price
    list_display = ['currency', 'value', ]
    list_editable = ['value', ]


