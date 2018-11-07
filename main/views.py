from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic
from django_filters.views import FilterView
from django_tables2 import SingleTableView, SingleTableMixin, RequestConfig
from .forms import SignUpForm
from .models import Employee, DeletedEmployee
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from .filters import EmployeesFilter
from .tables import EmployeeTable
from django.contrib.auth import login, authenticate


def custom_table(request):

    all_employees = Employee.objects.all()
    data = request.GET.copy()
    my_filter = EmployeesFilter(data, queryset=all_employees)
    employees_table = EmployeeTable(my_filter.qs)
    employees_table.paginate(page=request.GET.get('page', 1), per_page=5)
    return render(request, 'employees_table.html', {'table1': employees_table, 'filter': my_filter})


def delete_employee(request):

    if request.method == "POST":
        pks = request.POST.getlist("selection")
        selected_objects = Employee.objects.filter(pk__in=pks)
        for deleted_employee in selected_objects:
            i = 0
            deleted_employee = selected_objects.get(pk=pks[i])
            deleted_employee = DeletedEmployee(name=deleted_employee.name, surname=deleted_employee.surname,
                                           hours=deleted_employee.hours, hourly_pay=deleted_employee.hourly_pay,
                                           wage_gross=deleted_employee.wage_gross, wage_net=deleted_employee.wage_net)
            deleted_employee.save()
            i += 1

        selected_objects.delete()
        return redirect('/main/employees/')


def main_page(request):
    return render(request, 'index.html')


class AddEmployee(LoginRequiredMixin, CreateView):
    model = Employee, DeletedEmployee
    template_name = 'employee_form.html'
    fields = ['name', 'surname', 'hours', 'hourly_pay', 'wage_gross', 'wage_net']


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/main/employees/')
    else:
        form = SignUpForm()

    return render(request, 'registration/register.html', {'form': form})


class DeletedEmployeeTable(SingleTableView):
    model = DeletedEmployee
    template_name = 'deleted_employees_table.html'
