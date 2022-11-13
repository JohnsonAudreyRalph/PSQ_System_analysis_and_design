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