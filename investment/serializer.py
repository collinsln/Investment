from rest_framework import serializers
from .models import Investor
from .models import InvestmentAccount
from .models import Transaction
from .models import InvestorAccountPermission

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ['id', 'name', 'email']

class InvestmentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentAccount
        fields = ['id', 'name']

class InvestorAccountPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorAccountPermission
        fields = ['id', 'investor', 'account', 'permission']

class TransactionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'investor', 'amount', 'description', 'date']
