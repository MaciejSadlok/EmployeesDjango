from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic
from django_filters.views import FilterView
from django_tables2 import SingleTableView, SingleTableMixin

from .models import Employee
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from .filters import EmployeesFilter


class EmployeesTableView(SingleTableMixin, FilterView):
    model = Employee
    template_name = 'employees_table.html'
    paginate_by = 10
    filterset_class = EmployeesFilter




def main_page(request):
    return render(request, 'index.html')


class DeleteEmployee(DeleteView):
    model = Employee
    success_url = reverse_lazy('main:all-employees')


class AddEmployee(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = ['name', 'surname', 'hours', 'hourly_pay', 'wage_gross', 'wage_net']



