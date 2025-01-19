from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions


class IsOwnerAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return True
        try:
            return request.user == view.get_object()
        except:
            return False
