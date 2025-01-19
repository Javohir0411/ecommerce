from rest_framework.permissions import BasePermission


class IsOwnerOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        try:
            return request.user == view.get_object()
        except:
            return False
