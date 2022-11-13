from django import forms
from .models import BillOfDelivery, BillOfReturnGoodsBack, BillOfReturnTheGoods, BillOfImport

class Add_Bill_of_Return_the_Goods_Forms(forms.ModelForm):
    class Meta:
        model = BillOfReturnTheGoods
        fields = ('matrahang', 'thoigian', 'makhachhang')

class Add_Bill_of_Return_Goods_Back_Forms(forms.ModelForm):
    class Meta:
        model = BillOfReturnGoodsBack
        fields = ('ngaytra', 'tenncc', 'tongtienhangtra', 'tongtienncccantra', 'nccdatra', 'trangthai')

class Add_Bill_of_Devicery_Forms(forms.ModelForm):
    class Meta:
        model = BillOfDelivery
        fields = ('maphieuchuyen', 'tudiadiem', 'dendiadiem', 'trangthai')

class Add_Bill_of_Import_Forms(forms.ModelForm):
    class Meta:
        model = BillOfImport
        fields = ('mahoadon', 'manhacungcap', 'ngaynhap', 'tongtien', 'datra', 'trangthai')