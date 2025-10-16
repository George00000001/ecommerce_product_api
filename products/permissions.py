from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only the product owner can edit or delete.
    """
    def has_object_permission(self, request, view, obj):
        # Read-only methods (GET, HEAD, OPTIONS) are always allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise, only allow if the user owns the object
        return obj.user == request.user
