from django.shortcuts import render, redirect
from django.views import View
from .models import ProductModel, PresicriptionModel, DrugInventory
from .forms import Add_Product_Forms, Add_Prescription_Froms, Add_DrugInventory_From
import pyodbc
# Define Connection String
conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=DESKTOP-2B5FRR5;'
        'Database=System_analysis_and_design;'
        'Trusted_Connection=yes;'
    )

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
        if request.method == "POST":
            ma_hang = request.POST.get('ma_hang')
            ten_hang = request.POST.get('ten_hang')
            don_vi = request.POST.get('don_vi')
            gia_goc = request.POST.get('gia_goc')
            gia_ban = request.POST.get('gia_ban')
            so_luong_ton_kho = request.POST.get('so_luong_ton_kho')
            trang_thai = request.POST.get('trang_thai')
            print('Đang INSERT');
            print('Mã hàng là: '+ ma_hang)
            print('Tên hàng là: '+ ten_hang)
            print('Đơn vị là: '+ don_vi)
            print('Giá gốc là: '+ gia_goc)
            print('Giá bán là: '+ gia_ban)
            print('Số lượng tồn kho là: '+ so_luong_ton_kho)
            print('Trạng thái là: '+ trang_thai)

            cursor = conn.cursor();
            SQLCommand = ("INSERT INTO [System_analysis_and_design].[dbo].[Product_model](Ma_Hang, Ten_Hang, Don_Vi, Gia_Goc, Gia_Ban, So_Luong_Ton_Kho, Trang_Thai) VALUES(?, ?, ?, ?, ?, ?, ?);")
            Values = [ma_hang, ten_hang, don_vi, gia_goc, gia_ban, so_luong_ton_kho, trang_thai]
            try:
                cursor.execute(SQLCommand,Values)
            except Exception as e:
                cursor.rollback()
                print('Lỗi gì đó rồi đấy')
                
            else:
                print('records inserted successfully')
                cursor.commit()
                cursor.close()
                return redirect('/Commodity/Product/')
        else:
            return render(request, 'Commodity/Product.html')

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
        print('Mã hàng là: '+ ma_hang)
        print('Tên hàng là: '+ ten_hang)
        print('Đơn vị là: '+ don_vi)
        print('Giá gốc là: '+ gia_goc)
        print('Giá bán là: '+ gia_ban)
        print('Số lượng tồn kho là: '+ so_luong_ton_kho)
        print('Trạng thái là: '+ trang_thai)
        cursor = conn.cursor();
        cursor.execute('UPDATE [System_analysis_and_design].[dbo].[Product_model] set Ma_Hang = ?, Ten_Hang = ?, Don_Vi = ?, Gia_Goc = ?, Gia_Ban = ?, So_Luong_Ton_Kho = ?, Trang_Thai = ? WHERE id=?', (ma_hang, ten_hang, don_vi, gia_goc, gia_ban, so_luong_ton_kho, trang_thai, id));
        cursor.commit()
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
        # ngay_nhap = request.POST.get('ngay_nhap')
        ma_thuoc = request.POST.get('ma_thuoc')
        ten_thuoc = request.POST.get('ten_thuoc')
        don_vi = request.POST.get('don_vi')
        so_luong_dung = request.POST.get('so_luong_dung')
        lieu_dung = request.POST.get('lieu_dung')
        trang_thai_thuoc = request.POST.get('trang_thai_thuoc')
        ghi_chu = request.POST.get('ghi_chu')
        cursor = conn.cursor();
        cursor.execute('UPDATE [System_analysis_and_design].[dbo].[Presicription_model] SET Ma_Thuoc = ?, Ten_Thuoc = ?, Don_Vi = ?, So_Luong_Dung = ?, Lieu_Dung = ?, Trang_Thai_Thuoc = ?, Ghi_Chu = ? WHERE id = ?', (ma_thuoc, ten_thuoc, don_vi, so_luong_dung, lieu_dung, trang_thai_thuoc, ghi_chu, id));
        cursor.commit()
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
        # thoigiankiemkho = request.POST.get('thoigiankiemkho')
        mahang = request.POST.get('mahang')
        so_luong_ton_kho = request.POST.get('so_luong_ton_kho')
        danh_gia_thuoc = request.POST.get('danh_gia_thuoc')

        cursor = conn.cursor();
        cursor.execute('UPDATE [System_analysis_and_design].[dbo].[Drug_Inventory] SET MaKiemKho = ?, MaHang = ?, So_Luong_Ton_Kho = ?, Danh_Gia_Thuoc = ? WHERE id = ?', (makiemkho, mahang, so_luong_ton_kho, danh_gia_thuoc, id));
        cursor.commit()
        return redirect('/Commodity/Drug_inventory/')
    return render(request, 'Commodity/Drug_inventory.html')