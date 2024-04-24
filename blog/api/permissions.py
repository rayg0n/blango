from rest_framework import permissions

class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.Safe_Methods:
      return true

    return request.user == obj.author

class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)
