# investment_app/serializers.py
from rest_framework import serializers
from investment_app.models import Trade, CashFlow  # Import your Trade model

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['loan_id', 'investment_date', 'maturity_date', 'interest_rate']  # Add your model fields here

class CashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlow
        fields = ['cashflow_id', 'loan', 'cashflow_date', 'cashflow_currency', 'cashflow_type', 'amount']  # Add your model fields here
