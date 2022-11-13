# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

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

class Supplier(models.Model):
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
