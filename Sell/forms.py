from django import forms
from Transaction.models import BillOfSale

class Add_BillOfSale_Forms(forms.ModelForm):
    class Meta:
        model = BillOfSale
        fields = ('madonhang', 'thoigian', 'matrahang', 'loaikhachhang', 'tongtien', 'giamgia', 'khachhangtra')