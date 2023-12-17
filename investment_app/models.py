from django.db import models

# Trade model
class Trade(models.Model):
    loan_id = models.CharField(primary_key=True, max_length=50)
    investment_date = models.DateField()
    maturity_date = models.DateField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

# CashFlow model
class CashFlow(models.Model):
    cashflow_id = models.CharField(primary_key=True, max_length=50) 
    loan = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name='cashflows')  
    cashflow_date = models.DateField()
    cashflow_currency = models.CharField(max_length=3)  
    cashflow_type = models.CharField(max_length=30)  
    amount = models.DecimalField(max_digits=12, decimal_places=2) 