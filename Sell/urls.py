from django.urls import path
from .views import *
app_name = 'Sell'
urlpatterns = [
    path('Sell/', Sell.as_view(), name='Sell'),
    path('Sell/Add_BillOfSale', Add_BillOfSale.as_view(), name='Add_BillOfSale')
]