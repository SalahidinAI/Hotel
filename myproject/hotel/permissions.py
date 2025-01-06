from rest_framework import permissions


class CheckStatus(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_status == 'owner'


class CheckClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_status == 'client'


class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_status == 'owner'


class ClientBooking(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.user_status == 'owner'


class CheckBooking(permissions.BasePermission):
    pass


class OwnerBooking(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_status == 'owner'