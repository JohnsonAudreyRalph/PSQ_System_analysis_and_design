from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Supplier
from .forms import Add_Customer_Forms, Add_Supplier_Forms
# Create your views here.
class Customer_Show(View):
    def get(self, request):
        # Customer_data = Customer.objects.all()
        # return render(request, 'Interactive/Customer.html', {'Customer_data':Customer_data})
        return render(request, 'Interactive/Customer.html')


class Add_Customer(View):
    def get(self, request):
        fm = Add_Customer_Forms()
        # return render(request, 'Interactive/Customer.html', {'Forms':fm})
        return render(request, 'Interactive/Customer.html')
    def post(self, request):
        return render(request, 'Interactive/Customer.html')
        fm = Add_Customer_Forms(request.POST)
        # if fm.is_valid():
        #     fm.save()
        #     return redirect('/Interactive/Customer/')
        # else:
        #     # return render(request, 'Interactive/Customer.html', {'Forms':fm})

def UPDATE_Customer(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        makhachhang = request.POST.get('makhachhang')
        tenkhachhang = request.POST.get('tenkhachhang')
        masothue = request.POST.get('masothue')
        dienthoai = request.POST.get('dienthoai')
        gioitinh = request.POST.get('gioitinh')
        ngaysinh = request.POST.get('ngaysinh')
        email = request.POST.get('email')
        congty = request.POST.get('congty')
        diachi = request.POST.get('diachi')
        loaikhachhang = request.POST.get('loaikhachhang')
        # Customer_dt = Customer(
        #     id = id,
        #     makhachhang = makhachhang,
        #     tenkhachhang = tenkhachhang,
        #     masothue = masothue,
        #     dienthoai = dienthoai,
        #     gioitinh = gioitinh,
        #     ngaysinh = ngaysinh,
        #     email = email,
        #     congty = congty,
        #     diachi = diachi,
        #     loaikhachhang = loaikhachhang
        # )
        # Customer_dt.save()
        # return redirect('/Interactive/Customer/')
    return render(request, 'Interactive/Customer.html')

class Supplier_Show(View):
    def get(self, request):
        # Supplier_data = Supplier.objects.all()
        # return render(request, 'Interactive/Supplier.html', {'Supplier_data':Supplier_data})
        return render(request, 'Interactive/Supplier.html')

class Add_Supplier(View):
    def get(self, request):
        # fm = Add_Supplier_Forms()
        # return render(request, 'Interactive/Supplier.html', {'Forms':fm})
        return render(request, 'Interactive/Supplier.html')
    def post(self, request):
        return render(request, 'Interactive/Supplier.html')
        # fm = Add_Supplier_Forms(request.POST)
        # if fm.is_valid():
        #     fm.save()
        #     return redirect('/Interactive/Supplier/')
        # else:
        #     return render(request, 'Interactive/Supplier.html', {'Forms':fm})

def UPDATE_Supplier(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        manhacungcap = request.POST.get('manhacungcap')
        tenncc = request.POST.get('tenncc')
        email = request.POST.get('email')
        dienthoai = request.POST.get('dienthoai')
        congty = request.POST.get('congty')
        diachi = request.POST.get('diachi')
        masothue = request.POST.get('masothue')
        # Supplier_dt = Supplier(
        #     id = id,
        #     manhacungcap = manhacungcap,
        #     tenncc = tenncc,
        #     email = email,
        #     dienthoai = dienthoai,
        #     congty = congty,
        #     diachi = diachi,
        #     masothue = masothue,
        # )
        # Supplier_dt.save()
        # return redirect('/Interactive/Supplier/')
    return render(request, 'Interactive/Supplier.html')