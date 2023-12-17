from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TradeSerializer, CashFlowSerializer
import pandas as pd
from investment_app.models import Trade, CashFlow
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from datetime import datetime
from django.utils import timezone
from rest_framework.decorators import api_view
from django.shortcuts import render

# View for the home page.
def home(request):
    return render(request, 'home.html')

# API view for uploading Trade data.
class TradeUploadView(APIView):
    def post(self, request, format=None):
        file = request.FILES['file']
        df = pd.read_excel(file)
        for _, row in df.iterrows(): 
              Trade.objects.create( 
                loan_id=row['loan_id'], 
                investment_date=pd.to_datetime(row['investment_date'], format='%d/%m/%Y').date(), 
                maturity_date=pd.to_datetime(row['maturity_date'], format='%d/%m/%Y').date(), 
                interest_rate=float(row['interest_rate'].replace('%', '').strip()) 
            )        
        return Response({'message': 'Trades uploaded successfully'}, status=status.HTTP_200_OK)

# API view for uploading CashFlow data.
class CashFlowUploadView(APIView):
    def post(self, request, format=None):
        file = request.FILES['file']
        df = pd.read_excel(file)  
        for _, row in df.iterrows(): 
            loan_instance = Trade.objects.get(loan_id=row['loan_id'])  
            CashFlow.objects.create(       
                cashflow_id=row['cashflow_id'],  
                loan=loan_instance,  
                cashflow_date=pd.to_datetime(row['cashflow_date'], format='%d/%m/%Y').date(), 
                cashflow_currency=row['cashflow_currency'],  
                cashflow_type=row['cashflow_type'], 
                amount=abs(float(row['amount'].replace(',', '').strip())) 
            )
        return Response({'message': 'Cash flows uploaded successfully'}, status=status.HTTP_200_OK)

# API view to get the realized amount by a given date.
@api_view(['GET'])
def get_realized_amount(request, year, month, day):
    reference_date = datetime(year, month, day).date()
    realized_amount = CashFlow.objects.filter(
        cashflow_date__lte=reference_date,
        cashflow_type='repayment'
    ).aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    return JsonResponse({'realized_amount': realized_amount})

# Function to calculate the gross expected amount as of a reference date.
def calculate_gross_expected_amount(reference_date):
    gross_expected_amount = 0
    for trade in Trade.objects.all():
        funding_amount = trade.cashflows.filter(
            cashflow_type='funding',
            cashflow_date__lte=reference_date
        ).aggregate(total_amount=Sum('amount'))['total_amount'] or 0

        passed_days = (reference_date - trade.investment_date).days
        daily_interest_rate = trade.interest_rate / 36500
        gross_expected_interest_amount = funding_amount * daily_interest_rate * passed_days

        gross_expected_amount += funding_amount + gross_expected_interest_amount

    return gross_expected_amount

# API view to get the gross expected amount by a given date.
@api_view(['GET'])
def get_gross_expected_amount(request, year, month, day):
    reference_date = datetime(year, month, day).date()
    amount = calculate_gross_expected_amount(reference_date)
    return JsonResponse({'gross_expected_amount': amount})

# API view to get the remaining invested amount by a given date.
@api_view(['GET'])
def get_remaining_invested_amount(request, year, month, day):
    reference_date = datetime(year, month, day).date()
    invested_amount = CashFlow.objects.filter(
        cashflow_type='funding',
        cashflow_date__lte=reference_date
    ).aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    realized_amount = CashFlow.objects.filter(
        cashflow_type='repayment',
        cashflow_date__lte=reference_date
    ).aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    remaining_invested_amount = invested_amount - realized_amount
    return JsonResponse({'remaining_invested_amount': remaining_invested_amount})


# API view to get the closing date of a trade given its ID.
@api_view(['GET'])
def get_closing_date(request, trade_id):
    try:
        trade = Trade.objects.get(loan_id=trade_id)  
    except Trade.DoesNotExist:
        return JsonResponse({'error': 'Trade not found'}, status=404)

    realized_amount = 0
    closing_date = None

    for cashflow in trade.cashflows.all():  
        if cashflow.cashflow_type == "repayment":
            realized_amount += cashflow.amount
            if realized_amount >= calculate_gross_expected_amount(cashflow.cashflow_date):
                closing_date = cashflow.cashflow_date.strftime('%Y-%m-%d')
                break

    return JsonResponse({'closing_date': closing_date})