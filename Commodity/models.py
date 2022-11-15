# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BillOfDelivery(models.Model):
    maphieuchuyen = models.CharField(db_column='MaPhieuChuyen', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tudiadiem = models.TextField(db_column='TuDiaDiem', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dendiadiem = models.TextField(db_column='DenDiaDiem', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    trangthai = models.CharField(db_column='TrangThai', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bill_of_Delivery'
        unique_together = (('id', 'maphieuchuyen'),)


class BillOfImport(models.Model):
    mahoadon = models.CharField(db_column='MaHoaDon', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    manhacungcap = models.CharField(db_column='MaNhaCungCap', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ngaynhap = models.DateField(db_column='NgayNhap', blank=True, null=True)  # Field name made lowercase.
    tongtien = models.IntegerField(db_column='TongTien', blank=True, null=True)  # Field name made lowercase.
    datra = models.IntegerField(db_column='DaTra', blank=True, null=True)  # Field name made lowercase.
    trangthai = models.CharField(db_column='TrangThai', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bill_of_Import'
        unique_together = (('id', 'mahoadon'),)


class BillOfReturnGoodsBack(models.Model):
    ngaytra = models.DateField(db_column='NgayTra', blank=True, null=True)  # Field name made lowercase.
    tenncc = models.TextField(db_column='TenNCC', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tongtienhangtra = models.IntegerField(db_column='TongTienHangTra', blank=True, null=True)  # Field name made lowercase.
    tongtienncccantra = models.IntegerField(db_column='TongTienNCCCanTra', blank=True, null=True)  # Field name made lowercase.
    nccdatra = models.IntegerField(db_column='NCCDaTra', blank=True, null=True)  # Field name made lowercase.
    trangthai = models.TextField(db_column='TrangThai', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bill_of_Return_Goods_Back'


class BillOfReturnTheGoods(models.Model):
    matrahang = models.CharField(db_column='MaTraHang', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    thoigian = models.DateField(db_column='ThoiGian', blank=True, null=True)  # Field name made lowercase.
    makhachhang = models.CharField(db_column='MaKhachHang', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bill_of_Return_the_Goods'
        unique_together = (('id', 'matrahang'),)


class BillOfSale(models.Model):
    madonhang = models.CharField(db_column='MaDonHang', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    thoigian = models.DateField(db_column='ThoiGian', blank=True, null=True)  # Field name made lowercase.
    matrahang = models.CharField(db_column='MaTraHang', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    loaikhachhang = models.CharField(db_column='LoaiKhachHang', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tongtien = models.IntegerField(db_column='TongTien', blank=True, null=True)  # Field name made lowercase.
    giamgia = models.IntegerField(db_column='GiamGia', blank=True, null=True)  # Field name made lowercase.
    khachhangtra = models.IntegerField(db_column='KhachHangTra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bill_of_Sale'
        unique_together = (('id', 'madonhang'),)


class Customer(models.Model):
    makhachhang = models.CharField(db_column='MaKhachHang', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tenkhachhang = models.TextField(db_column='TenKhachHang', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    masothue = models.CharField(db_column='MaSoThue', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dienthoai = models.CharField(db_column='DienThoai', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gioitinh = models.CharField(db_column='GioiTinh', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ngaysinh = models.DateField(db_column='NgaySinh', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    congty = models.TextField(db_column='CongTy', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diachi = models.TextField(db_column='DiaChi', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    loaikhachhang = models.CharField(db_column='LoaiKhachHang', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'
        unique_together = (('id', 'makhachhang'),)


class DebtCllectionReport(models.Model):
    tenkhachhang = models.TextField(db_column='TenKhachHang', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    congnodauky = models.IntegerField(db_column='CongNoDauKy', blank=True, null=True)  # Field name made lowercase.
    congnocuoiky = models.IntegerField(db_column='CongNoCuoiky', blank=True, null=True)  # Field name made lowercase.
    trangthai = models.CharField(db_column='TrangThai', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tungay = models.DateField(db_column='TuNgay')  # Field name made lowercase.
    denngay = models.DateField(db_column='DenNgay')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Debt_Cllection_Report'


class DebtPaymentReport(models.Model):
    tennhacungcap = models.TextField(db_column='TenNhaCungCap', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    congnodauky = models.IntegerField(db_column='CongNoDauKy', blank=True, null=True)  # Field name made lowercase.
    congnocuoiky = models.IntegerField(db_column='CongNoCuoiKy', blank=True, null=True)  # Field name made lowercase.
    trangthai = models.IntegerField(db_column='TrangThai', blank=True, null=True)  # Field name made lowercase.
    tungay = models.DateField(db_column='TuNgay')  # Field name made lowercase.
    denngay = models.DateField(db_column='DenNgay')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Debt_Payment_Report'


class DrugInventory(models.Model):
    makiemkho = models.CharField(db_column='MaKiemKho', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    thoigiankiemkho = models.DateField(db_column='ThoiGianKiemKho', blank=True, null=True)  # Field name made lowercase.
    mahang = models.CharField(db_column='MaHang', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    so_luong_ton_kho = models.IntegerField(db_column='So_Luong_Ton_Kho', blank=True, null=True)  # Field name made lowercase.
    danh_gia_thuoc = models.TextField(db_column='Danh_Gia_Thuoc', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Drug_Inventory'
        unique_together = (('id', 'makiemkho'),)


class PresicriptionModel(models.Model):
    ngay_nhap = models.DateField(db_column='Ngay_Nhap', blank=True, null=True)  # Field name made lowercase.
    ma_thuoc = models.CharField(db_column='Ma_Thuoc', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ten_thuoc = models.TextField(db_column='Ten_Thuoc', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    don_vi = models.TextField(db_column='Don_Vi', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    so_luong_dung = models.IntegerField(db_column='So_Luong_Dung', blank=True, null=True)  # Field name made lowercase.
    lieu_dung = models.TextField(db_column='Lieu_Dung', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    trang_thai_thuoc = models.TextField(db_column='Trang_Thai_Thuoc', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ghi_chu = models.TextField(db_column='Ghi_Chu', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presicription_model'
        unique_together = (('id', 'ma_thuoc'),)


class ProductModel(models.Model):
    ma_hang = models.CharField(db_column='Ma_Hang', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ten_hang = models.TextField(db_column='Ten_Hang', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    don_vi = models.CharField(db_column='Don_Vi', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gia_goc = models.IntegerField(db_column='Gia_Goc', blank=True, null=True)  # Field name made lowercase.
    gia_ban = models.IntegerField(db_column='Gia_Ban', blank=True, null=True)  # Field name made lowercase.
    so_luong_ton_kho = models.IntegerField(db_column='So_Luong_Ton_Kho', blank=True, null=True)  # Field name made lowercase.
    trang_thai = models.TextField(db_column='Trang_Thai', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product_model'
        unique_together = (('id', 'ma_hang'),)


class Supplier(models.Model):
    id = models.IntegerField(primary_key=True)
    manhacungcap = models.CharField(db_column='MaNhaCungCap', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tenncc = models.TextField(db_column='TenNCC', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dienthoai = models.CharField(db_column='DienThoai', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    congty = models.TextField(db_column='CongTy', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diachi = models.TextField(db_column='DiaChi', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    masothue = models.CharField(db_column='MaSoThue', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Supplier'
        unique_together = (('id', 'manhacungcap'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
