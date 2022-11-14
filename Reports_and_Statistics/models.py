# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

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