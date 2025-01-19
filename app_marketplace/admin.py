from django.contrib import admin

from .models import Product, Category, ProductReview, Cart, Order, Payment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name_uz', 'product_price', 'product_price_unit', 'product_category')
    search_fields = ('product_name_uz', 'product_name_ru', )
    ordering = ['id']


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name_uz', 'category_name_ru')
    search_fields = ('category_name_uz', 'category_name_ru', )
    ordering = ['id']


admin.site.register(Category, CategoryAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'rating')
    search_fields = ('product', )
    ordering = ['id']


admin.site.register(ProductReview, ProductReviewAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
    search_fields = ('product', )
    ordering = ['id']


admin.site.register(Cart, CartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price')
    search_fields = ('user', 'product', )
    ordering = ['id']


admin.site.register(Order, OrderAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'status')
    search_fields = ('order', )
    ordering = ['id']


admin.site.register(Payment, PaymentAdmin)
