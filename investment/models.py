from django.db import models

class Investor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

class InvestmentAccount(models.Model):
    name = models.CharField(max_length=100)
    investors = models.ManyToManyField(Investor, through='InvestorAccountPermission')

    def __str__(self):
        return self.name
    
class InvestorAccountPermission(models.Model):
    PERMISSION_CHOICES = [
        ('view', 'View Only'),
        ('full', 'Full Access'),
        ('transaction', 'Transaction Only'),
    ]
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)
    permission = models.CharField(max_length=20, choices=PERMISSION_CHOICES)

    def __str__(self):
        return f"{self.investor.name} - {self.account.name} - {self.permission}"
    
class Transaction(models.Model):
    account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction by {self.investor.name} on {self.date}: {self.amount} - {self.description}"

# class InvestorAccountPermission(models.Model):
#     PERMISSION_CHOICES = [
#         ('view', 'View Only'),
#         ('full', 'Full Access'),
#         ('transaction', 'Transaction Only'),
#     ]
#     investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
#     account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)
#     permission = models.CharField(max_length=20, choices=PERMISSION_CHOICES)

#     def __str__(self):
#         return f'{self.investor.name} - {self.account.name} ({self.get_permission_display()})'

# class Transaction(models.Model):
#     account = models.ForeignKey(InvestmentAccount, on_delete=models.CASCADE)
#     investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateTimeField(auto_now_add=True)
#     description = models.CharField(max_length=200)

#     def __str__(self):
#         return f'{self.account.name} - {self.amount} ({self.date})'
