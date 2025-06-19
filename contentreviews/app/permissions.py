from rest_framework import permissions
class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        if request.method == 'GET' or admin_permission:
            return True
        else:
            return False
class ReviewPermissions(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = bool(request.user)
        if request.method == 'GET' or is_authenticated:
            return True
        else:
            return False
