from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS


class OwnerOrAdminOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.author == user:
            return True
        return request.method in SAFE_METHODS or user.is_staff
