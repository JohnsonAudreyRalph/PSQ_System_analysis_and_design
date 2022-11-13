from django import forms
from .models import BillOfImport

class Add_Bill_of_Import_Forms(forms.ModelForm):
    class Meta:
        model = BillOfImport
        fields = ('mahoadon', 'manhacungcap', 'ngaynhap', 'tongtien', 'datra', 'trangthai')