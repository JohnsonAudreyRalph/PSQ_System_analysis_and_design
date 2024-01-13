from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'Login_Register/Login.html')
    
class Affter_Login(View):
    def get(self, request):
        return render(request, 'Overview/Overview_Interface.html')
    
class Register(View):
    def get(self, request):
        return render(request, 'Login_Register/Register.html')
    def post(self, request):
        if request.method == "POST":
            First_Name = request.POST.get('First_Name')
            Last_Name = request.POST.get('Last_Name')
            email = request.POST.get('Email_Address')
            username = request.POST.get('User_Name')
            Password = request.POST.get('Password')
            Confirm_Password = request.POST.get('Confirm_Password')
            # =============================== catch errors when registering ===============================
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username")
                return render(request, 'Login_Register/Register.html')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already Register")
                return render(request, 'Login_Register/Register.html')
            
            if Password!=Confirm_Password:
                messages.error(request, "Password didn't match!")
                print('Chưa lưu')
                return render(request, 'Login_Register/Register.html')

            MyUser = User.objects.create_user(username, email, Password)
            MyUser.First_Name = First_Name
            MyUser.Last_Name = Last_Name
            MyUser.save()

            print('Họ tên: ' + First_Name + " " + Last_Name)
            print('Email: ' + email)
            print('User Name: ' + username)
            print('Password: ' + Password)
            print('Config Password: ' + Confirm_Password)
            return render(request, 'Login_Register/Login.html')
        return render(request, 'Login_Register/Register.html')

class Login(View):
    def get(self, request):
        return render(request, 'Login_Register/Login.html')
    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('User_Name')
            Password = request.POST.get('Password')
            user = authenticate(username=username, password=Password)
            if user is not None:
                login(request, user)
                return redirect('/Login_Success/')
            else:
                messages.error(request, "BAD")
                return HttpResponse('EROR')

def Logout(request):
    logout(request)
    return render(request, 'Login_Register/Logout.html')