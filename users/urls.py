from rest_framework import routers
from django.urls import path
from users.views import (
    RegisterAPIView,
    ProfileUpdateView,
    password_change_view,
    password_reset_view,
    LoginAPIView,
    LogoutAPIView,
)
router = routers.DefaultRouter()
router.register(r'profile', ProfileUpdateView, basename='profile')

urlpatterns = router.urls

urlpatterns += [
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('password-change/', password_change_view, name="password-change"),
    path('password-reset/', password_reset_view, name="password-reset"),
    path('api/login/', LoginAPIView.as_view(), name='api-login'),
    path('api/logout/', LogoutAPIView.as_view(), name='api-logout'),
]
