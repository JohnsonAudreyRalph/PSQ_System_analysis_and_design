# Generated by Django 4.2 on 2023-04-12 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('makhachhang', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MaKhachHang', max_length=10)),
                ('tenkhachhang', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TenKhachHang', null=True)),
                ('masothue', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MaSoThue', max_length=10, null=True)),
                ('dienthoai', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DienThoai', max_length=12, null=True)),
                ('gioitinh', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='GioiTinh', max_length=50, null=True)),
                ('ngaysinh', models.DateField(blank=True, db_column='NgaySinh', null=True)),
                ('email', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Email', max_length=255, null=True)),
                ('congty', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CongTy', null=True)),
                ('diachi', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DiaChi', null=True)),
                ('loaikhachhang', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='LoaiKhachHang', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manhacungcap', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MaNhaCungCap', max_length=10)),
                ('tenncc', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TenNCC', null=True)),
                ('email', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Email', null=True)),
                ('dienthoai', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DienThoai', max_length=12, null=True)),
                ('congty', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CongTy', null=True)),
                ('diachi', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DiaChi', null=True)),
                ('masothue', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MaSoThue', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Supplier',
                'managed': False,
            },
        ),
    ]
