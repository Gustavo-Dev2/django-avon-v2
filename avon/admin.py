from django.contrib import admin
from .models import Category, Brand, Product, Image

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Mostramos estos campos en la lista
    search_fields = ('name',)  # Habilitamos búsqueda por nombre

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available', 'category', 'brand')
    list_filter = ('category', 'brand', 'available')  # Filtros en la barra lateral
    search_fields = ('name',)  # Búsqueda por nombre
    autocomplete_fields = ['category', 'brand']  # Autocompletado para categorías y marcas

class ImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'product', 'image_url')
    search_fields = ('alt_text', 'product__name')  # Búsqueda por texto alternativo y nombre del producto



# Registramos los modelos en el admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
# Registra el modelo Image con su admin personalizado
admin.site.register(Image, ImageAdmin)
