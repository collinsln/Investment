from django.contrib import admin
from .models import Investor
from .models import InvestmentAccount
from .models import Transaction

admin.site.register(Investor)
admin.site.register(InvestmentAccount)
admin.site.register(Transaction)