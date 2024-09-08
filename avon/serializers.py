from rest_framework import serializers
from .models import Category, Brand, Product, Image

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'description']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_url', 'alt_text', 'product']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'available', 'category', 'brand', 'images']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("The price must be greater than 0.")
        return value

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("The name must be at least 3 characters long.")
        return value

    def validate(self, data):
        if data['category'] is None or data['brand'] is None:
            raise serializers.ValidationError("Category and Brand are required.")
        return data
