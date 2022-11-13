from django import forms
from .models import Customer, Supplier

class Add_Customer_Forms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('makhachhang', 'tenkhachhang', 'masothue', 'dienthoai', 'gioitinh', 'ngaysinh', 'email', 'congty', 'diachi', 'loaikhachhang')

class Add_Supplier_Forms(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('manhacungcap', 'tenncc', 'email', 'dienthoai', 'congty', 'diachi', 'masothue')