from django import forms
from .models import ProductModel, PresicriptionModel, DrugInventory
class Add_Product_Forms(forms.ModelForm):
    class Meta:
        UNIT_TYPES = (
            ('Vỉ', 'Vỉ'),
            ('Hộp', 'Hộp'),
            ('Tuýp', 'Tuýp'),
            ('Lọ', 'Lọ'),
            ('Chai', 'Chai'),
            ('Viên', 'Viên'),
            ('Cái', 'Cái'),
            ('Gói', 'Gói')
        )
        STATUS_TYPES = (
            ('Đang kinh doanh', 'Đang kinh doanh'),
            ('Ngừng kinh doanh', 'Ngừng kinh doanh')
        )
        model = ProductModel
        fields = ('ma_hang', 'ten_hang', 'don_vi', 'gia_goc', 'gia_ban', 'so_luong_ton_kho', 'trang_thai')
        widgets = {
            'ma_hang':forms.TextInput(attrs={'class':'form-control'}),
            'ten_hang':forms.TextInput(attrs={'class':'form-control'}),
            'don_vi':forms.Select(
                attrs={'class':'form-control'},
                choices=UNIT_TYPES,
            ),
            'gia_goc':forms.NumberInput(attrs={'class':'form-control'}),
            'gia_ban':forms.NumberInput(attrs={'class':'form-control'}),
            'so_luong_ton_kho':forms.NumberInput(attrs={'class':'form-control'}),
            'trang_thai':forms.Select(
                attrs={'class':'form-control'},
                choices=STATUS_TYPES,
            ),
        }


class Add_Prescription_Froms(forms.ModelForm):
    class Meta:
        UNIT_TYPES = (
            ('Vỉ', 'Vỉ'),
            ('Hộp', 'Hộp'),
            ('Tuýp', 'Tuýp'),
            ('Lọ', 'Lọ'),
            ('Chai', 'Chai'),
            ('Viên', 'Viên'),
            ('Cái', 'Cái'),
            ('Gói', 'Gói')
        )
        STATUS_TYPES = (
            ('Áp dụng', 'Áp dụng'),
            ('Chưa áp dụng', 'Chưa áp dụng')
        )
        model = PresicriptionModel
        fields = ('ngay_nhap', 'ma_thuoc', 'ten_thuoc', 'don_vi', 'so_luong_dung', 'lieu_dung', 'trang_thai_thuoc', 'ghi_chu')
        widgets = {
            'ngay_nhap':forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
            'ma_thuoc':forms.TextInput(attrs={'class':'form-control'}),
            'ten_thuoc':forms.TextInput(attrs={'class':'form-control'}),
            'don_vi':forms.Select(
                attrs={'class':'form-control'},
                choices=UNIT_TYPES,
            ),
            'so_luong_dung':forms.NumberInput(attrs={'class':'form-control'}),
            'lieu_dung':forms.TextInput(attrs={'class':'form-control'}),
            'trang_thai_thuoc':forms.Select(
                attrs={'class':'form-control'},
                choices=STATUS_TYPES,
            ),
            'ghi_chu':forms.Textarea(attrs={'class':'form-control'})
        }

class Add_DrugInventory_From(forms.ModelForm):
    class Meta:
        STATUS_TYPES = (
            ('Đảm bảo chất lượng', 'Đảm bảo chất lượng'),
            ('Không đảm bảo chất lượng', 'Không đảm bảo chất lượng')
        )
        model = DrugInventory
        fields = ('makiemkho', 'thoigiankiemkho', 'mahang','so_luong_ton_kho', 'danh_gia_thuoc')
        widgets = {
            'makiemkho':forms.TextInput(attrs={'class':'form-control'}),
            'thoigiankiemkho':forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
            'mahang':forms.TextInput(attrs={'class':'form-control'}),
            'so_luong_ton_kho':forms.NumberInput(attrs={'class':'form-control'}),
            'danh_gia_thuoc':forms.Select(
                attrs={'class':'form-control'},
                choices=STATUS_TYPES,
            ),
        }