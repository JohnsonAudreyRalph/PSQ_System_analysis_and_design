from django.shortcuts import render, redirect
from django.views import View
# from Commodity.models import ProductModel
from .forms import Add_Bill_of_Import_Forms

# Create your views here.
class Import_Goods(View):
    def get(self, request):
        # Product_data = ProductModel.objects.all()
        # return render(request, 'Import_Goods/Import_Goods.html', {'Product_data':Product_data})
        return render(request, 'Import_Goods/Import_Goods.html')

class Add_Bill_of_Import(View):
    def post(self, request):
        return render(request, 'Import_Goods/Import_Goods.html')
        # fm = Add_Bill_of_Import_Forms(request.POST)
        # if fm.is_valid():
        #     fm.save()
        #     return redirect('/Import_Goods/Import_Goods/')
        # else:
        #     return render(request, 'Import_Goods/Import_Goods.html')
