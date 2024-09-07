# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_date
from django.db.models import Sum
from .models import Investor, InvestmentAccount, InvestorAccountPermission, Transaction
from .serializer import (InvestorSerializer, InvestmentAccountSerializer, 
                         InvestorAccountPermissionSerializer, TransactionSerializer)
from .permissions import InvestmentAccountPermissions, TransactionPermission



class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

class InvestmentAccountViewSet(viewsets.ModelViewSet):
    queryset = InvestmentAccount.objects.all()
    serializer_class = InvestmentAccountSerializer
    permission_classes = [InvestmentAccountPermissions]

class InvestorAccountPermissionViewSet(viewsets.ModelViewSet):
    queryset = InvestorAccountPermission.objects.all()
    serializer_class = InvestorAccountPermissionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [TransactionPermission]

class UserTransactionViewSet(viewsets.ViewSet):
    def list(self, request):
        # Extract start and end dates from request parameters
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response(
                {"detail": "Please provide both start_date and end_date parameters."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
        except (ValueError, TypeError):
            return Response(
                {"detail": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if start_date is None or end_date is None:
            return Response(
                {"detail": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if start_date > end_date:
            return Response(
                {"detail": "start_date cannot be after end_date."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Fetch transactions within the date range
        transactions = Transaction.objects.filter(date__range=[start_date, end_date])
        serializer = TransactionSerializer(transactions, many=True)

        # Calculate total balance
        total_balance = transactions.aggregate(total=Sum('amount'))['total'] or 0

        return Response({
            'transactions': serializer.data,
            'total_balance': total_balance
        })

class AdminTransactionViewSet(viewsets.ViewSet):
    def list(self, request):
        if not request.user.is_superuser:
            return Response({"detail": "You do not have permission to access this resource."}, status=status.HTTP_403_FORBIDDEN)

        # Extract start and end dates from request parameters
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response(
                {"detail": "Please provide both start_date and end_date parameters."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
        except (ValueError, TypeError):
            return Response(
                {"detail": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if start_date is None or end_date is None:
            return Response(
                {"detail": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if start_date > end_date:
            return Response(
                {"detail": "start_date cannot be after end_date."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Fetch all transactions within the date range
        transactions = Transaction.objects.filter(date__range=[start_date, end_date])
        serializer = TransactionSerializer(transactions, many=True)

        # Calculate total balance
        total_balance = transactions.aggregate(total=Sum('amount'))['total'] or 0

        return Response({
            'transactions': serializer.data,
            'total_balance': total_balance
        })
