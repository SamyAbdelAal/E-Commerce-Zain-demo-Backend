from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    message = "This is not your profile"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.user == request.user:
            return True
        return False
class IsUserOrder(BasePermission):
    message = "This is not your profile"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.ordered_by == request.user:
            return True
        return False