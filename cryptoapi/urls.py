from django.urls import path
from .views import main, CryptocurrencyList, CryptocurrencyUpdate, CryptocurrencyBySymbolView

urlpatterns = [
    path('', main),
    path('prices/', CryptocurrencyList.as_view(), name='cryptocurrency-list'),
    path('prices/update/<str:symbol>/', CryptocurrencyUpdate.as_view(), name='cryptocurrency-update'),
    path('prices/<str:symbol>/', CryptocurrencyBySymbolView.as_view(), name='cryptocurrency-selectOne')
]
