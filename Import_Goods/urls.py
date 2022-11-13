from django.urls import path
from .views import *
app_name = 'Import_Goods'
urlpatterns = [
    path('Import_Goods/', Import_Goods.as_view(), name='Import_Goods'),
    path('Import_Goods/Add_Bill_of_Import/', Add_Bill_of_Import.as_view(), name='Add_Bill_of_Import'),
]