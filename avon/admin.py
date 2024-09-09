from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Brand, Product, Image

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'category', 'brand', 'image_preview')
    list_filter = ('category', 'brand', 'available')
    search_fields = ('name',)
    autocomplete_fields = ['category', 'brand']

    def image_preview(self, obj):
        if obj.images.exists():
            first_image = obj.images.first()
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', first_image.image_url.url)
        return 'No Image'
    image_preview.short_description = 'Image Preview'

class ImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'product', 'image_url')
    search_fields = ('alt_text', 'product__name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
