from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Employee, DeletedEmployee
from django.views.generic.edit import CreateView
from .filters import EmployeesFilter, DeletedEmployeesFilter
from .tables import EmployeeTable, DeletedEmployeeTable
from django.contrib.auth import login, authenticate


# this view returns employees table with pagination and possibility to search one.
def employees(request):
    all_employees = Employee.objects.all()
    data = request.GET.copy()
    my_filter = EmployeesFilter(data, queryset=all_employees)
    employees_table = EmployeeTable(my_filter.qs)
    employees_table.paginate(page=request.GET.get('page', 1), per_page=5)
    return render(request, 'employees_table.html', {'table1': employees_table, 'filter': my_filter})


# this view deletes employee/s and make copy of deletion in new model.
def delete_employee(request):
    if request.method == "POST":
        pks = request.POST.getlist("selection")
        selected_objects = Employee.objects.filter(pk__in=pks)
        for deleted_employee in range(len(pks)):
            deleted_employee = selected_objects.get(pk=pks[0])
            deleted_employee = DeletedEmployee(name=deleted_employee.name, surname=deleted_employee.surname,
                                           hours=deleted_employee.hours, hourly_pay=deleted_employee.hourly_pay,
                                           wage_gross=deleted_employee.wage_gross, wage_net=deleted_employee.wage_net)
            deleted_employee.save()
            del pks[0]
        selected_objects.delete()
        return redirect('/main/employees/')


# this views returns deleted employees table with pagination and possibility to search one.
def deleted_employees(request):
    all_deleted_employees = DeletedEmployee.objects.all()
    data = request.GET.copy()
    my_filter = DeletedEmployeesFilter(data, queryset=all_deleted_employees)
    deleted_employees_table = DeletedEmployeeTable(my_filter.qs)
    deleted_employees_table.paginate(page=request.GET.get('page', 1), per_page=5)
    return render(request, 'deleted_employees_table.html', {'table1': deleted_employees_table, 'filter': my_filter})


# this view deletes deleted employees forever.
def hard_delete_employee(request):
    if request.method == "POST":
        pks = request.POST.getlist("selection")
        selected_objects = DeletedEmployee.objects.filter(pk__in=pks)
        selected_objects.delete()
        return redirect('/main/deleted_employees/')


# this view returns index page.
def main_page(request):
    return render(request, 'index.html')


# this view returns form for creating new employee, requires being logged in.
class AddEmployee(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'add_employee_form.html'
    fields = ['name', 'surname', 'hours', 'hourly_pay', 'wage_gross', 'wage_net']


# this view returns form for user's registration.
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



