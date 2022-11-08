from django.shortcuts import render, redirect
from django.views import View
from .models import ProductModel, PresicriptionModel, DrugInventory
from .forms import Add_Product_Forms, Add_Prescription_Froms, Add_DrugInventory_From

# Create your views here.
class Product(View):
    def get(self, request):
        Product_data = ProductModel.objects.all()
        return render(request, 'Commodity/Product.html', {'Product_data':Product_data})

class Add_Product(View):
    def get(self, request):
        fm = Add_Product_Forms()
        return render(request, 'Commodity/Product.html', {'Forms':fm})
    def post(self, request):
        fm = Add_Product_Forms(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/Commodity/Product/')
        else:
            return render(request, 'Commodity/Product.html', {'Forms':fm})

def EDIT(request):
    Product_data = ProductModel.objects.all()
    return render(request, 'Commodity/Product.html', {'Product_data':Product_data})

def UPDATE(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        ma_hang = request.POST.get('ma_hang')
        ten_hang = request.POST.get('ten_hang')
        don_vi = request.POST.get('don_vi')
        gia_goc = request.POST.get('gia_goc')
        gia_ban = request.POST.get('gia_ban')
        so_luong_ton_kho = request.POST.get('so_luong_ton_kho')
        trang_thai = request.POST.get('trang_thai')
        Product_dt = ProductModel(
            id = id,
            ma_hang = ma_hang,
            ten_hang = ten_hang,
            don_vi = don_vi,
            gia_goc = gia_goc,
            gia_ban = gia_ban,
            so_luong_ton_kho = so_luong_ton_kho,
            trang_thai = trang_thai,
        )
        Product_dt.save()
        return redirect('/Commodity/Product/')
    return render(request, 'Commodity/Product.html')

class Prescription(View):
    def get(self, request):
        Prescription_data = PresicriptionModel.objects.all()
        return render(request, 'Commodity/Prescription.html', {'Prescription_data':Prescription_data})

class Add_Prescription(View):
    def get(self, request):
        fm = Add_Prescription_Froms()
        return render(request, 'Commodity/Prescription.html', {'Forms':fm})
    def post(self, request):
        fm = Add_Prescription_Froms(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/Commodity/Prescription')
        else:
            return render(request, 'Commodity/Prescription.html', {'Forms':fm})

def EDIT_Pre(request):
    Prescription_data = PresicriptionModel.objects.all()
    return render(request, 'Commodity/Prescription.html', {'Prescription_data':Prescription_data})

def UPDATE_Pre(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        ngay_nhap = request.POST.get('ngay_nhap')
        ma_thuoc = request.POST.get('ma_thuoc')
        ten_thuoc = request.POST.get('ten_thuoc')
        don_vi = request.POST.get('don_vi')
        so_luong_dung = request.POST.get('so_luong_dung')
        lieu_dung = request.POST.get('lieu_dung')
        trang_thai_thuoc = request.POST.get('trang_thai_thuoc')
        ghi_chu = request.POST.get('ghi_chu')
        Prescription_dt = PresicriptionModel(
            id = id,
            ngay_nhap = ngay_nhap,
            ma_thuoc = ma_thuoc,
            ten_thuoc = ten_thuoc,
            don_vi = don_vi,
            so_luong_dung = so_luong_dung,
            lieu_dung = lieu_dung,
            trang_thai_thuoc = trang_thai_thuoc,
            ghi_chu = ghi_chu,
        )
        Prescription_dt.save()
        return redirect('/Commodity/Prescription/')
    return render(request, 'Commodity/Prescription.html')

class Price_setting(View):
    def get(self, request):
        Product_data = ProductModel.objects.all()
        return render(request, 'Commodity/Price_setting.html', {'Product_data':Product_data})

def UPDATE_Price(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        ma_hang = request.POST.get('ma_hang')
        ten_hang = request.POST.get('ten_hang')
        don_vi = request.POST.get('don_vi')
        gia_goc = request.POST.get('gia_goc')
        gia_ban = request.POST.get('gia_ban')
        so_luong_ton_kho = request.POST.get('so_luong_ton_kho')
        trang_thai = request.POST.get('trang_thai')
        Product_Price_dt = ProductModel(
            id = id,
            ma_hang = ma_hang,
            ten_hang = ten_hang,
            don_vi = don_vi,
            gia_goc = gia_goc,
            gia_ban = gia_ban,
            so_luong_ton_kho = so_luong_ton_kho,
            trang_thai = trang_thai,
        )
        Product_Price_dt.save()
        return redirect('/Commodity/Price_setting/')
    return render(request, 'Commodity/Price_setting.html')



class Drug_inventory(View):
    def get(self, request):
        DrugInventory_data = DrugInventory.objects.all()
        return render(request, 'Commodity/Drug_inventory.html', {'DrugInventory_data':DrugInventory_data})

class Add_Drug_inventory(View):
    def get(self, request):
        fm = Add_DrugInventory_From()
        return render(request, 'Commodity/Drug_inventory.html', {'Forms':fm})
    def post(self, request):
        fm = Add_DrugInventory_From(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/Commodity/Drug_inventory/')
        else:
            return render(request, 'Commodity/Drug_inventory.html', {'Forms':fm})

def UPDATE_Drug_inventory(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        makiemkho = request.POST.get('makiemkho')
        thoigiankiemkho = request.POST.get('thoigiankiemkho')
        mahang = request.POST.get('mahang')
        so_luong_ton_kho = request.POST.get('so_luong_ton_kho')
        danh_gia_thuoc = request.POST.get('danh_gia_thuoc')
        Drug_inventory_dt = DrugInventory(
            id = id,
            makiemkho = makiemkho,
            thoigiankiemkho = thoigiankiemkho,
            mahang = mahang,
            so_luong_ton_kho = so_luong_ton_kho,
            danh_gia_thuoc = danh_gia_thuoc,
        )
        Drug_inventory_dt.save()
        return redirect('/Commodity/Drug_inventory/')
    return render(request, 'Commodity/Drug_inventory.html')