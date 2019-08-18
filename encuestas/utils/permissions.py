# Django Rest
from rest_framework.permissions import BasePermission

class IsUserOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

class IsEmpresaOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.empresa == obj.empresa