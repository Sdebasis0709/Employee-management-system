# employees/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm  # Import your EmployeeForm

def index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'form': form})

def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/update_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('index')

    return render(request, 'employees/delete_employee.html', {'employee': employee})




print("cdhjlkxjbsaxc b")







print("pulleddddddddddddddddddddddddddddddddddddd")