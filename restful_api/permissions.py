from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """ Permission that will only allow the user that created the object to change it.  Allows others to read. """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.username == request.user
