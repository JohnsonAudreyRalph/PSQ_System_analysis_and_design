from django.urls import path, include
from .views import *
app_name = 'Transaction'
urlpatterns = [
    path('Bill_of_Sale/', Bill_of_Sale.as_view(), name='Bill_of_Sale'),
    path('Bill_of_Sale/Bill_of_Sale_UPDATE/<str:id>', Bill_of_Sale_UPDATE, name='Bill_of_Sale_UPDATE'),

    path('Bill_of_Import/', Bill_of_Import.as_view(), name='Bill_of_Import'),
    path('Bill_of_Import/Bill_of_Import_UPDATE/<str:id>', Bill_of_Import_UPDATE, name='Bill_of_Import_UPDATE'),

    path('Bill_of_Return_the_Goods/', Bill_of_Return_the_Goods.as_view(), name='Bill_of_Return_the_Goods'),
    path('Bill_of_Return_the_Goods/Add_Bill_of_Return_the_Goods/', Add_Bill_of_Return_the_Goods.as_view(), name='Add_Bill_of_Return_the_Goods'),
    path('Bill_of_Return_the_Goods/UPDATE_Bill_of_Return_the_Goods/<str:id>', UPDATE_Bill_of_Return_the_Goods, name='UPDATE_Bill_of_Return_the_Goods'),

    path('Bill_of_Return_Goods_Back/', Bill_of_Return_Goods_Back.as_view(), name='Bill_of_Return_Goods_Back'),
    path('Bill_of_Return_Goods_Back/Add_Bill_of_Return_Goods_Back/', Add_Bill_of_Return_Goods_Back.as_view(), name='Add_Bill_of_Return_Goods_Back'),
    path('Bill_of_Return_Goods_Back/UPDATE_Bill_of_Return_Goods_Back/<str:id>', UPDATE_Bill_of_Return_Goods_Back, name='UPDATE_Bill_of_Return_Goods_Back'),

    path('Bill_of_Delivery/', Bill_of_Delivery.as_view(), name='Bill_of_Delivery'),
    path('Bill_of_Delivery/Add_Bill_of_Devicery/', Add_Bill_of_Devicery.as_view(), name='Add_Bill_of_Devicery'),
    path('Bill_of_Delivery/UPDATE_Bill_of_Delivery/<str:id>', UPDATE_Bill_of_Delivery, name='UPDATE_Bill_of_Delivery'),

]