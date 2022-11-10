from django import forms
from .models import BillOfDelivery, BillOfImport, BillOfReturnGoodsBack, BillOfReturnTheGoods, BillOfSale

class Add_Bill_of_Return_the_Goods_Forms(forms.ModelForm):
    class Meta:
        model = BillOfReturnTheGoods
        fields = ('matrahang', 'thoigian', 'makhachhang')

class Add_Bill_of_Return_Goods_Back_Forms(forms.ModelForm):
    class Meta:
        model = BillOfReturnGoodsBack
        fields = ('ngaytra', 'tenncc', 'tongtienhangtra', 'tongtienncccantra', 'nccdatra', 'trangthai')