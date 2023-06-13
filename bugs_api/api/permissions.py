from rest_framework import permissions


class IsBugOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, bug_obj):
        return bug_obj.user.id == request.user.id
