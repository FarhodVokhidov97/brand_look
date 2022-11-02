from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    raw_id_fields = ['product']


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    raw_id_fields = ['product']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'stock', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'stock', 'available')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    inlines = (ProductImagesInline, CharacteristicInline)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)