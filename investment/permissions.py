# permissions.py
from rest_framework import permissions
from .models import InvestorAccountPermission

class InvestmentAccountPermissions(permissions.BasePermission):
    """
    Custom permissions for Investment Account access.
    """

    def has_object_permission(self, request, view, obj):
        # Get the permission for the investor and account from the database
        try:
            permission = InvestorAccountPermission.objects.get(
                investor=request.user,
                account=obj
            ).permission
        except InvestorAccountPermission.DoesNotExist:
            return False

        if permission == 'view':
            return request.method in permissions.SAFE_METHODS
        elif permission == 'full':
            return True
        elif permission == 'transaction':
            return request.method in ['POST']
        return False

    def has_permission(self, request, view):
        # If the request is to list or retrieve objects, check the object-level permissions
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

class TransactionPermission(permissions.BasePermission):
    """
    Custom permissions for Transaction access.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user can access this transaction based on their permission
        try:
            permission = InvestorAccountPermission.objects.get(
                investor=request.user,
                account=obj.account
            ).permission
        except InvestorAccountPermission.DoesNotExist:
            return False

        if permission == 'view':
            return False  # Cannot view transactions
        elif permission == 'full':
            return True  # Can view and create transactions
        elif permission == 'transaction':
            return request.method == 'POST'  # Only allow POST requests
        return False
