from django.urls import path
from .views import *
app_name = 'Login_Register'
urlpatterns = [
    path('Login_Success/', Affter_Login.as_view(), name='Affter_Login'),
    path('', Login.as_view(), name='Login'),
    path('Register/', Register.as_view(), name='Register'),
    path('Logout/', Logout, name='Logout')
]