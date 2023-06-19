from django.shortcuts import render, redirect
from django.views import View
from .models import DebtCllectionReport, DebtPaymentReport
# Create your views here.
# import pyodbc
# Define Connection String
# conn = pyodbc.connect(
#         'Driver={ODBC Driver 17 for SQL Server};'
#         'Server=DESKTOP-2B5FRR5;'
#         'Database=System_analysis_and_design;'
#         'Trusted_Connection=yes;'
#     )


class Debt_Cllection_Report(View):
    def get(self, request):
        return render(request, 'Reports_and_Statistics/Debt_Cllection_Report.html')
        # Debt_Cllection_Report_data = DebtCllectionReport.objects.all()
        # return render(request, 'Reports_and_Statistics/Debt_Cllection_Report.html', {'Debt_Cllection_Report_data':Debt_Cllection_Report_data})

class Add_Debt_Cllection_Report(View):
    def post(self, request):
        if request.method == "POST":
            tenkhachhang = request.POST.get('tenkhachhang')
            congnodauky = request.POST.get('congnodauky')
            congnocuoiky = request.POST.get('congnocuoiky')
            trangthai = int(congnocuoiky) - int(congnodauky)
            tungay = request.POST.get('tungay')
            denngay = request.POST.get('denngay')
            # Debt_Cllection_Report_dt = DebtCllectionReport(
            #     tenkhachhang = tenkhachhang,
            #     congnodauky = congnodauky,
            #     congnocuoiky = congnocuoiky,
            #     trangthai = trangthai,
            #     tungay = tungay,
            #     denngay = denngay,
            # )
            # Debt_Cllection_Report_dt.save()
            # return redirect('/Reports_and_Statistics/Debt_Cllection_Report/')
        return render(request, 'Reports_and_Statistics/Debt_Cllection_Report.html')

def UPDATE_Debt_Cllection_Report(request, id):
    if request.method == "POST":
        tenkhachhang = request.POST.get('tenkhachhang')
        congnodauky = request.POST.get('congnodauky')
        congnocuoiky = request.POST.get('congnocuoiky')
        # trangthai = int(congnocuoiky) - int(congnodauky)
        # cursor = conn.cursor();
        # cursor.execute('UPDATE [System_analysis_and_design].[dbo].[Debt_Cllection_Report] SET TenKhachHang = ?, CongNoDauKy = ?, CongNoCuoiky = ?, TrangThai = ? WHERE id = ?', (tenkhachhang, congnodauky, congnocuoiky, trangthai, id));
        # cursor.commit()
        # return redirect('/Reports_and_Statistics/Debt_Cllection_Report/')
    return render(request, 'Reports_and_Statistics/Debt_Cllection_Report.html')

class Debt_Payment_Report(View):
    def get(self, request):
        # Debt_Payment_Report_data = DebtPaymentReport.objects.all()
        # return render(request, 'Reports_and_Statistics/Debt_Payment_Report.html', {'Debt_Payment_Report_data':Debt_Payment_Report_data})
        return render(request, 'Reports_and_Statistics/Debt_Payment_Report.html')

class Add_Debt_Payment_Report(View):
    def post(self, request):
        if request.method == "POST":
            print("Nhận giá trị rồi")
            tennhacungcap = request.POST.get('tennhacungcap')
            congnodauky = request.POST.get('congnodauky')
            congnocuoiky = request.POST.get('congnocuoiky')
            # trangthai = int(congnocuoiky) - int(congnodauky)
            tungay = request.POST.get('tungay')
            # denngay = request.POST.get('denngay')
            # Debt_Payment_Report_dt = DebtPaymentReport(
            #     tennhacungcap = tennhacungcap,
            #     congnodauky = congnodauky,
            #     congnocuoiky = congnocuoiky,
            #     trangthai = trangthai,
            #     tungay = tungay,
            #     denngay = denngay,
            # )
            # Debt_Payment_Report_dt.save()
            # return redirect('/Reports_and_Statistics/Debt_Payment_Report/')
        return render(request, 'Reports_and_Statistics/Debt_Payment_Report.html')

def UPDATE_Debt_Payment_Report(request, id):
    if request.method == "POST":
        print("Nhận giá trị rồi")
        tennhacungcap = request.POST.get('tennhacungcap')
        congnodauky = request.POST.get('congnodauky')
        congnocuoiky = request.POST.get('congnocuoiky')
        trangthai = int(congnocuoiky) - int(congnodauky)
        tungay = request.POST.get('tungay')
        denngay = request.POST.get('denngay')
        # cursor = conn.cursor();
        # cursor.execute('UPDATE [System_analysis_and_design].[dbo].[Debt_Payment_Report] SET TenNhaCungCap = ?, CongNoDauKy = ?, CongNoCuoiky = ?, TrangThai = ? WHERE id = ?', (tennhacungcap, congnodauky, congnocuoiky, trangthai, id));
        # cursor.commit()
        # return redirect('/Reports_and_Statistics/Debt_Payment_Report/')
    return render(request, 'Reports_and_Statistics/Debt_Payment_Report.html')









from .models import BillOfImport, BillOfSale

class Income_Statistics(View):
    def get(self, request):
        Bill_of_Import_data = BillOfImport.objects.all() #Hóa đơn nhập
        Bill_of_Sale_data = BillOfSale.objects.all() #Hóa đơn bán
        # context = {
        #     "Bill_of_Import": Bill_of_Import_data,
        #     "Bill_of_Sale": Bill_of_Sale_data
        # }
        # return render(request, 'Reports_and_Statistics/Income_Statistics.html', context)
        return render(request, 'Reports_and_Statistics/Income_Statistics.html')