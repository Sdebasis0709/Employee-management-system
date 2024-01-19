# employees/forms.py

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter employee name'}),
            'designation': forms.TextInput(attrs={'placeholder': 'Enter employee designation'}),
            'salary': forms.NumberInput(attrs={'placeholder': 'Enter employee salary'}),
            'join_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
        labels = {
            'name': 'Employee Name',
            'designation': 'Employee Designation',
            'salary': 'Employee Salary',
            'join_date': 'Join Date',
        }
