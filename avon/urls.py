from django.urls import path
from .views import (
    CategoryListCreateAPIView, CategoryDetailAPIView,
    BrandListCreateAPIView, BrandDetailAPIView,
    ProductListCreateAPIView, ProductDetailAPIView,
    ImageListCreateAPIView, ImageDetailAPIView
)

app_name= 'avon'

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),

    path('brands/', BrandListCreateAPIView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailAPIView.as_view(), name='brand-detail'),

    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),

    path('images/', ImageListCreateAPIView.as_view(), name='image-list'),
    path('images/<int:pk>/', ImageDetailAPIView.as_view(), name='image-detail'),
]
