# permissions.py
from rest_framework import permissions

class GroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # check if user is super user
        
        # Check if the user belongs to the 'Administrator' group
        if request.user.groups.filter(name='Administrator').exists():
            return True

        # Check if the user belongs to the 'Store Keeper' group and is accessing 'Item' or 'Category' views
        if (
            request.user.groups.filter(name='Store Keeper').exists()
            and view.__class__.__name__ in ['ItemViewSet', 'CategoryViewSet']
        ):
            return True

        return False
