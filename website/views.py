from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Employee

# Create your views here.

def home(request):
    employee_list = Employee.objects.all()
    return render(request, 'website/home.html', {'emp_list' : employee_list})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been authenticated and logged in successfully')
            return redirect('home')
        else:
            messages.success(request, 'Login failed, try again!')
            return redirect('login')
    else:
        return render(request, 'website/login.html', {})          

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('home')

def employee_view(request, pk):
    if request.user.is_authenticated:
        current_employee = Employee.objects.get(pk=pk)
        return render(request, 'website/employee.html', {'emp' : current_employee})
    else:
        messages.success(request, 'You need to be logged in to see employee details')
        return redirect('home')
    
def delete(request, pk):
    if request.user.is_authenticated:
        current_employee = Employee.objects.get(pk=pk)
        current_employee.delete()
        return redirect('home')
    else:
        messages.success(request, 'You need to be logged in delete the employee')
        return redirect('home')

