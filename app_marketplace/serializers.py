from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from app_marketplace.models import (Product,
                                    Category,
                                    Order,
                                    Cart,
                                    Payment,
                                    ProductReview)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        field = '__all__'


class CategoryGetSerializer(ModelSerializer):
    category_name = SerializerMethodField(method_name='get_category_name', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'category_name')

    def get_category_name(self, obj):
        try:
            if self.context['request']['lang'] == 'ru':
                return obj.category_name_ru
            return obj.category_name_uz
        except:
            return obj.category_name_uz


# Product Serializer
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductGetSerializer(ModelSerializer):
    product_name = SerializerMethodField(method_name='get_product_name', read_only=True)
    product_description = SerializerMethodField(method_name='get_product_description', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'product_name', 'product_price', 'product_price_unit', 'product_description', 'product_category'
        )

    def get_product_name(self, obj):
        try:
            if self.context['request']['lang'] == 'ru':
                return obj.product_name_ru
            return obj.product_name_uz
        except:
            return obj.product_name_uz

    def get_product_description(self, obj):
        try:
            if self.context['request']['lang'] == 'ru':
                return obj.product_description_ru
            return obj.product_description_uz
        except:
            return obj.product_description_uz


class OrderSerializer(ModelSerializer):
    class Meta:
        model = "Order"
        fields = "__all__"


class OrderGetSerializer(ModelSerializer):
    class Meta:
        model = "Order"
        fields = (
            'id', 'product_name', 'quantity', 'total_price'
        )


class CartSerializer(ModelSerializer):
    class Meta:
        model = 'Cart'
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = 'Payment'
        fields = "__all__"


class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = "ProductReview"
        fields = "__all__"


class ProductReviewGetSerializer(ModelSerializer):
    class Meta:
        model = "ProductReview"
        fields = (
            "id", "product", "rating"
        )
