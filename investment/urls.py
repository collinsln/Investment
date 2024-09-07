# urls.py
# urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (InvestorViewSet, InvestmentAccountViewSet, 
                    InvestorAccountPermissionViewSet, TransactionViewSet, 
                    UserTransactionViewSet, AdminTransactionViewSet)

router = DefaultRouter()
router.register(r'investors', InvestorViewSet)
router.register(r'investment-accounts', InvestmentAccountViewSet)
router.register(r'investor-permissions', InvestorAccountPermissionViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include(router.urls)),
    path('user-transactions/', UserTransactionViewSet.as_view({'get': 'list'}), name='user-transactions'),
    path('admin-transactions/', AdminTransactionViewSet.as_view({'get': 'list'}), name='admin-transactions'),
]

