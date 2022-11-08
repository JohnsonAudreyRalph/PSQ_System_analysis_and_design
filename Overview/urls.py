from django.urls import path
from .views import *
app_name = 'Overview'
urlpatterns = [
    path('Overview/', Overview.as_view(), name='Overview')
]