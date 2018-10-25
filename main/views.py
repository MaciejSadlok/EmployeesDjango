from django.shortcuts import render
from .models import Employee
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees_table.html', {'employees': employees})


class DeleteEmployee(DeleteView):
    model = Employee
    success_url = reverse_lazy('main:all_employees')

