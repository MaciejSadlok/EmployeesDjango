from django.shortcuts import render
from .models import Employee


def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees_table.html', {'employees': employees})



