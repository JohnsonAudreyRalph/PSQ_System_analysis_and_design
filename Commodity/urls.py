from django.urls import path
from .views import *
app_name = 'Commodity'
urlpatterns = [
    path('Product/', Product.as_view(), name='Product'),
    path('Product/Add_Product/', Add_Product.as_view(), name='Add_Product'),
    path('Product/Edit/', EDIT, name='Edit'),
    path('Product/Update/<str:id>', UPDATE, name='Update'),

    path('Prescription/', Prescription.as_view(), name='Prescription'),
    path('Prescription/Add_Prescription/', Add_Prescription.as_view(), name='Add_Prescription'),
    path('Prescription/Edit/', EDIT_Pre, name = 'EDIT_Pre'),
    path('Prescription/Update_Pre/<str:id>', UPDATE_Pre, name='Update_Pre'),

    path('Price_setting/', Price_setting.as_view(), name='Price_setting'),
    path('Price_setting/Update_Price/<str:id>', UPDATE_Price, name='Update_Price'),
    
    path('Drug_inventory/', Drug_inventory.as_view(), name='Drug_inventory'),
    path('Drug_inventory/Add_Drug_inventory/', Add_Drug_inventory.as_view(), name='Add_Drug_inventory'),
    path('Drug_inventory/UPDATE_Drug_inventory/<str:id>', UPDATE_Drug_inventory, name='UPDATE_Drug_inventory'),
]