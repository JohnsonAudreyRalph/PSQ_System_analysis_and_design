from django.urls import path
from .views import *
app_name = 'Interactive'
urlpatterns = [
    path('Customer/', Customer_Show.as_view(), name='Customer'),
    path('Customer/Add_Customer/', Add_Customer.as_view(), name='Add_Customer'),
    path('Customer/UPDATE_Customer/<str:id>', UPDATE_Customer, name='UPDATE_Customer'),

    path('Supplier/', Supplier_Show.as_view(), name='Supplier'),
    path('Supplier/Add_Supplier/', Add_Supplier.as_view(), name='Add_Supplier'),
    path('Supplier/UPDATE_Supplier/<str:id>', UPDATE_Supplier, name='UPDATE_Supplier'),
]