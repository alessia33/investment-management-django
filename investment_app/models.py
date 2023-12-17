from django.db import models

# Create your models here.
class Trade(models.Model):
    loan_id = models.CharField(primary_key=True, max_length=50)
    investment_date = models.DateField()
    maturity_date = models.DateField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

class CashFlow(models.Model):
    cashflow_id = models.CharField(primary_key=True, max_length=50) # use this field as the primary key ,  the values in this field must be unique for each record in the table.
    loan = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name='cashflows') #It means that each cash flow is associated with a particular trade. 
                    #  if a trade is deleted, all associated cash flows should also be deleted. related_name='cashflows' option provides a reverse relationship name,
                    # allowing you to access the cash flows associated with a trade using the cashflows attribute.
    cashflow_date = models.DateField()
    cashflow_currency = models.CharField(max_length=3)  
    cashflow_type = models.CharField(max_length=30)  
    amount = models.DecimalField(max_digits=12, decimal_places=2) 