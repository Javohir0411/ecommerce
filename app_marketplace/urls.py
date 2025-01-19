from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import (register_view,
                    login_view,
                    CartViewSet,
                    ProductViewSet,
                    OrderViewSet,
                    CategoryViewSet,
                    PaymentViewSet,
                    ProductReviewViewSet
                    )
from django.urls import path

router = routers.DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"product", ProductViewSet, basename="product")
router.register(r"order", OrderViewSet, basename="order")
router.register(r"cart", CartViewSet, basename="cart")
router.register(r"payment", PaymentViewSet, basename="payment")
router.register(r"product_review", ProductReviewViewSet, basename="product_review")
urlpatterns = router.urls

urlpatterns += [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
