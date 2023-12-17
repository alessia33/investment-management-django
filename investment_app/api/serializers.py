# investment_app/serializers.py
from rest_framework import serializers
from investment_app.models import Trade, CashFlow  # Import your Trade model

# A serializer class for the Trade model. This class handles the conversion between Trade model instances and JSON format.
class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['loan_id', 'investment_date', 'maturity_date', 'interest_rate']  # Add your model fields here

# A serializer class for the CashFlow model. This class handles the conversion between CashFlow model instances and JSON format.
class CashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlow
        fields = ['cashflow_id', 'loan', 'cashflow_date', 'cashflow_currency', 'cashflow_type', 'amount']  # Add your model fields here
