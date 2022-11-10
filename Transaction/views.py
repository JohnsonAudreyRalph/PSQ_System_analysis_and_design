from django.shortcuts import render, redirect
from django.views import View
from .models import BillOfDelivery, BillOfImport, BillOfReturnGoodsBack, BillOfReturnTheGoods, BillOfSale
from .forms import Add_Bill_of_Return_the_Goods_Forms, Add_Bill_of_Return_Goods_Back_Forms
# Create your views here.
class Bill_of_Sale(View):
    def get(self, request):
        Bill_of_Sale_data = BillOfSale.objects.all()
        return render(request, 'Transaction/Bill_of_Sale.html', {'Bill_of_Sale_data':Bill_of_Sale_data})

def Bill_of_Sale_UPDATE(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        madonhang = request.POST.get('madonhang')
        thoigian = request.POST.get('thoigian')
        matrahang = request.POST.get('matrahang')
        loaikhachhang = request.POST.get('loaikhachhang')
        tongtien = request.POST.get('tongtien')
        giamgia = request.POST.get('giamgia')
        khachhangtra = request.POST.get('khachhangtra')
        Bill_of_Sale_dt = BillOfSale(
            id = id,
            madonhang = madonhang,
            thoigian = thoigian,
            matrahang = matrahang,
            loaikhachhang = loaikhachhang,
            tongtien = tongtien,
            giamgia = giamgia,
            khachhangtra = khachhangtra,
        )
        Bill_of_Sale_dt.save()
        return redirect('/Transaction/Bill_of_Sale/')
    return render(request, 'Transaction/Bill_of_Sale.html')

class Bill_of_Import(View):
    def get(self, request):
        Bill_of_Import_data = BillOfImport.objects.all()
        return render(request, 'Transaction/Bill_of_Import.html', {'Bill_of_Import_data':Bill_of_Import_data})

def Bill_of_Import_UPDATE(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        ngaynhap = request.POST.get('ngaynhap')
        tongtien = request.POST.get('tongtien')
        datra = request.POST.get('datra')
        trangthai = request.POST.get('trangthai')
        Bill_of_Import_dt = BillOfImport(
            id = id,
            ngaynhap = ngaynhap,
            tongtien = tongtien,
            datra = datra,
            trangthai = trangthai,
        )
        Bill_of_Import_dt.save()
        return redirect('/Transaction/Bill_of_Import/')
    return render(request, 'Transaction/Bill_of_Import.html')

class Bill_of_Return_the_Goods(View):
    def get(self, request):
        Bill_of_Return_the_Goods_data = BillOfReturnTheGoods.objects.all()
        return render(request, 'Transaction/Bill_of_Return_the_Goods.html', {'Bill_of_Return_the_Goods_data':Bill_of_Return_the_Goods_data})

class Add_Bill_of_Return_the_Goods(View):
    def post(self, request):
        fm = Add_Bill_of_Return_the_Goods_Forms(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/Transaction/Bill_of_Return_the_Goods/')
        else:
            return render(request, 'Transaction/Bill_of_Return_the_Goods.html')

def UPDATE_Bill_of_Return_the_Goods(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        matrahang = request.POST.get('matrahang')
        thoigian = request.POST.get('thoigian')
        makhachhang = request.POST.get('makhachhang')
        Bill_of_Return_the_Goods_dt = BillOfReturnTheGoods(
            id = id,
            matrahang = matrahang,
            thoigian = thoigian,
            makhachhang = makhachhang,
        )
        Bill_of_Return_the_Goods_dt.save()
        return redirect('/Transaction/Bill_of_Return_the_Goods/')
    return render(request, 'Transaction/Bill_of_Return_the_Goods.html')

class Bill_of_Return_Goods_Back(View):
    def get(self, request):
        Bill_of_Return_Goods_Back_data = BillOfReturnGoodsBack.objects.all()
        return render(request, 'Transaction/Bill_of_Return_Goods_Back.html', {'Bill_of_Return_Goods_Back_data':Bill_of_Return_Goods_Back_data})

class Add_Bill_of_Return_Goods_Back(View):
    def post(self, request):
        fm = Add_Bill_of_Return_Goods_Back_Forms(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/Transaction/Bill_of_Return_Goods_Back/')
        else:
            return render(request, 'Transaction/Bill_of_Return_Goods_Back.html')

def UPDATE_Bill_of_Return_Goods_Back(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        ngaytra = request.POST.get('ngaytra')
        tenncc = request.POST.get('tenncc')
        tongtienhangtra = request.POST.get('tongtienhangtra')
        tongtienncccantra = request.POST.get('tongtienncccantra')
        nccdatra = request.POST.get('nccdatra')
        trangthai = request.POST.get('trangthai')
        Bill_of_Return_Goods_Back_dt = BillOfReturnGoodsBack(
            id = id,
            ngaytra = ngaytra,
            tenncc = tenncc,
            tongtienhangtra = tongtienhangtra,
            tongtienncccantra = tongtienncccantra,
            nccdatra = nccdatra,
            trangthai = trangthai,
        )
        Bill_of_Return_Goods_Back_dt.save()
        return redirect('/Transaction/Bill_of_Return_Goods_Back/')
    return render(request, 'Transaction/Bill_of_Return_Goods_Back.html')


class Bill_of_Delivery(View):
    def get(self, request):
        return render(request, 'Transaction/Bill_of_Delivery.html')