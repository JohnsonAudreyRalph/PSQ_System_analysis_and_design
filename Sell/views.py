from django.shortcuts import render, redirect
from django.views import View
from .forms import Add_BillOfSale_Forms
# Create your views here.
class Sell(View):
    def get(self, request):
        return render(request, 'Sell/Sell.html')

class Add_BillOfSale(View):
    def post(self, request):
        fm = Add_BillOfSale_Forms(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request, 'Sell/Sell.html')
        else:
            return render(request, 'Sell/Sell.html')