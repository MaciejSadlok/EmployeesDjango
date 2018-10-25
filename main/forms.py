from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_surname', 'employee_hours', 'employee_hourly_pay',
                  'employee_wage_gross', 'employee_wage_net']

