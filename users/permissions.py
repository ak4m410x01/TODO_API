from rest_framework.permissions import BasePermission


class IsUserDetails(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user)
