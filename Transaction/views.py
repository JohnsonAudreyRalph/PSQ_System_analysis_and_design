from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from .models import BillOfDelivery, BillOfImport, BillOfReturnGoodsBack, BillOfReturnTheGoods, BillOfSale
from .forms import Add_Bill_of_Return_the_Goods_Forms, Add_Bill_of_Return_Goods_Back_Forms, Add_Bill_of_Devicery_Forms
# Create your views here.
import pyodbc
# Define Connection String
conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=DESKTOP-2B5FRR5;'
        'Database=System_analysis_and_design;'
        'Trusted_Connection=yes;'
    )

class Bill_of_Sale(View):
    def get(self, request):
        Bill_of_Sale_data = BillOfSale.objects.all()
        items = BillOfSale.objects.aggregate(TOTAL = Sum('tongtien'))['TOTAL']
        return render(request, 'Transaction/Bill_of_Sale.html', {'Bill_of_Sale_data':Bill_of_Sale_data, 'item':items})

def Bill_of_Sale_UPDATE(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        madonhang = request.POST.get('madonhang')
        matrahang = request.POST.get('matrahang')
        loaikhachhang = request.POST.get('loaikhachhang')
        tongtien = request.POST.get('tongtien')
        giamgia = request.POST.get('giamgia')
        khachhangtra = request.POST.get('khachhangtra')
        cursor = conn.cursor();
        cursor.execute('UPDATE [System_analysis_and_design].[dbo].[Bill_of_Sale] SET MaDonHang = ?, MaTraHang = ?, LoaiKhachHang = ?, TongTien = ?, GiamGia = ?, KhachHangTra = ? WHERE id = ?', (madonhang, matrahang, loaikhachhang, tongtien, giamgia, khachhangtra, id));
        cursor.commit()
        return redirect('/Transaction/Bill_of_Sale/')
    return render(request, 'Transaction/Bill_of_Sale.html')

class Bill_of_Import(View):
    def get(self, request):
        Bill_of_Import_data = BillOfImport.objects.all()
        items = BillOfImport.objects.aggregate(TOTAL = Sum('tongtien'))['TOTAL']
        return render(request, 'Transaction/Bill_of_Import.html', {'Bill_of_Import_data':Bill_of_Import_data, 'item':items})

def Bill_of_Import_UPDATE(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        manhacungcap = request.POST.get('manhacungcap')
        mahoadon = request.POST.get('mahoadon')
        tongtien = request.POST.get('tongtien')
        datra = request.POST.get('datra')
        trangthai = request.POST.get('trangthai')
        cursor = conn.cursor();
        cursor.execute('UPDATE [System_analysis_and_design].[dbo].[Bill_of_Import] SET MaHoaDon = ?, MaNhaCungCap = ?, TongTien = ?, DaTra = ?, TrangThai = ? WHERE id = ?', (mahoadon, manhacungcap, tongtien, datra, trangthai, id));
        cursor.commit()
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
        # thoigian = request.POST.get('thoigian')
        makhachhang = request.POST.get('makhachhang')
        cursor = conn.cursor();
        cursor.execute('UPDATE [System_analysis_and_design].[dbo].[Bill_of_Return_the_Goods] SET MaTraHang = ?, MaKhachHang = ? WHERE id = ?', (matrahang, makhachhang, id));
        cursor.commit()
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
        # ngaytra = request.POST.get('ngaytra')
        tenncc = request.POST.get('tenncc')
        tongtienhangtra = request.POST.get('tongtienhangtra')
        tongtienncccantra = request.POST.get('tongtienncccantra')
        nccdatra = request.POST.get('nccdatra')
        trangthai = request.POST.get('trangthai')
        cursor = conn.cursor();
        cursor.execute('UPDATE [System_analysis_and_design].[dbo].[Bill_of_Return_Goods_Back] SET TenNCC = ?, TongTienHangTra = ?, TongTienNCCCanTra = ?, NCCDaTra = ?, TrangThai = ? WHERE id = ?', (tenncc, tongtienhangtra, tongtienncccantra, nccdatra, trangthai, id));
        cursor.commit()
        return redirect('/Transaction/Bill_of_Return_Goods_Back/')
    return render(request, 'Transaction/Bill_of_Return_Goods_Back.html')


class Bill_of_Delivery(View):
    def get(self, request):
        Bill_of_Delivery_data = BillOfDelivery.objects.all()
        return render(request, 'Transaction/Bill_of_Delivery.html', {'Bill_of_Delivery_data':Bill_of_Delivery_data})

class Add_Bill_of_Devicery(View):
    def post(self, request):
        fm = Add_Bill_of_Devicery_Forms(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/Transaction/Bill_of_Delivery/')
        else:
            return render(request, 'Transaction/Bill_of_Delivery.html')

def UPDATE_Bill_of_Delivery(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        maphieuchuyen = request.POST.get('maphieuchuyen')
        tudiadiem = request.POST.get('tudiadiem')
        dendiadiem = request.POST.get('dendiadiem')
        trangthai = request.POST.get('trangthai')
        Bill_of_Delivery_dt = BillOfDelivery(
            id = id,
            maphieuchuyen = maphieuchuyen,
            tudiadiem = tudiadiem,
            dendiadiem = dendiadiem,
            trangthai = trangthai,
        )
        Bill_of_Delivery_dt.save()
        return redirect('/Transaction/Bill_of_Delivery/')
    return render(request, 'Transaction/Bill_of_Delivery.html')