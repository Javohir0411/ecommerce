from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(AbstractBaseModel):
    category_name_uz = models.CharField(max_length=255)
    category_name_ru = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category_name_uz} | {self.category_name_ru}"

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'category'


class Product(AbstractBaseModel):
    product_name_uz = models.CharField(max_length=255)
    product_name_ru = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_price_unit = models.CharField(max_length=5,
                                          choices=[('uzs', 'UZS'), ('usd', 'USD')],
                                          default='uzs')
    product_image = models.ImageField(upload_to='media/products_image/')
    product_description_uz = models.TextField()
    product_description_ru = models.TextField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name_uz} | Narxi: {self.product_price}"

    class Meta:
        verbose_name_plural = 'Products'
        db_table = 'product'


class Order(AbstractBaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.product and self.quantity:
            self.total_price = self.product.product_price * self.quantity
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} | {self.product}  | {self.quantity} | {self.total_price}"

    class Meta:
        verbose_name_plural = 'Orders'
        db_table = 'order'


class Cart(AbstractBaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user} | {self.product} | {self.quantity}"

    class Meta:
        verbose_name_plural = 'Cart'
        db_table = 'cart'


class Payment(AbstractBaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=100,
                              choices=[('pending', 'Pending'), ('completed', 'Completed'), ('fail', 'Fail')],
                              default='pending')

    def __str__(self):
        return f"Payment for order: {self.order.id}"

    class Meta:
        verbose_name_plural = "Payments"
        db_table = "payment"


class ProductReview(AbstractBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=[(1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')])
    review = models.TextField()

    def __str__(self):
        return f"Review for {self.product} by {self.user}"

    class Meta:
        verbose_name_plural = 'Product Reviews'
        verbose_name = 'Product Review'
        db_table = 'product_review'
