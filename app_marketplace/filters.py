from django_filters import rest_framework as filters
from app_marketplace.models import Category, Product


class ProductFilter(filters.FilterSet):
    product_name_uz = filters.CharFilter(lookup_expr='icontains')
    product_name_ru = filters.CharFilter(lookup_expr='icontains')
    product_descriptions_uz = filters.CharFilter(lookup_expr='icontains')
    product_descriptions_ru = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['product_name_uz', 'product_name_ru', 'product_descriptions_uz', 'product_descriptions_ru']


class CategoryFilter(filters.FilterSet):
    category_name_uz = filters.CharFilter(lookup_expr='icontains')
    category_name_ru = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['category_name_uz', 'category_name_ru']
