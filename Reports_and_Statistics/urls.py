from django.urls import path
from .views import *
app_name = 'Reports_and_Statistics'
urlpatterns = [
    path('Debt_Cllection_Report/', Debt_Cllection_Report.as_view(), name='Debt_Cllection_Report'),
    path('Debt_Cllection_Report/Add_Debt_Cllection_Report/', Add_Debt_Cllection_Report.as_view(), name='Add_Debt_Cllection_Report'),
    path('Debt_Cllection_Report/UPDATE_Debt_Cllection_Report/<str:id>', UPDATE_Debt_Cllection_Report, name='UPDATE_Debt_Cllection_Report'),

    path('Debt_Payment_Report/', Debt_Payment_Report.as_view(), name='Debt_Payment_Report'),
    path('Debt_Payment_Report/Add_Debt_Payment_Report/', Add_Debt_Payment_Report.as_view(), name='Add_Debt_Payment_Report'),
    path('Debt_Payment_Report/UPDATE_Debt_Payment_Report/<str:id>', UPDATE_Debt_Payment_Report, name='UPDATE_Debt_Payment_Report'),

    path('Income_Statistics/', Income_Statistics.as_view(), name='Income_Statistics'),
]