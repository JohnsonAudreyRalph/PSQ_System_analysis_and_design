# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DrugInventory(models.Model):
    makiemkho = models.CharField(db_column='MaKiemKho', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    thoigiankiemkho = models.DateField(db_column='ThoiGianKiemKho', blank=True, null=True)  # Field name made lowercase.
    mahang = models.CharField(db_column='MaHang', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    so_luong_ton_kho = models.IntegerField(db_column='So_Luong_Ton_Kho', blank=True, null=True)  # Field name made lowercase.
    danh_gia_thuoc = models.TextField(db_column='Danh_Gia_Thuoc', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Drug_Inventory'


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