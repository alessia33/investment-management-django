# investment_app/urls.py
from .views import home
from django.urls import path
from .views import TradeUploadView, CashFlowUploadView
from .views import get_realized_amount, get_remaining_invested_amount, get_gross_expected_amount, get_closing_date

# URL pattern configuration for the investment app
urlpatterns = [
    path('upload/trades/', TradeUploadView.as_view(), name='trade-upload'),
    path('upload/cashflows/', CashFlowUploadView.as_view(), name='cashflow-upload'),
    path('realized-amount/<int:year>/<int:month>/<int:day>/', get_realized_amount, name='get_realized_amount'),
    path('gross-expected-amount/<int:year>/<int:month>/<int:day>/', get_gross_expected_amount, name='get_gross_expected_amount'),  
    path('remaining-invested-amount/<int:year>/<int:month>/<int:day>/', get_remaining_invested_amount, name='get_remaining_invested_amount'),  
    path('closing-date/<str:trade_id>/', get_closing_date, name='get_closing_date'),
    path('' , home, name='home'), # This path renders the home page view.
]
