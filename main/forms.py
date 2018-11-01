from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'surname', 'hours', 'hourly_pay', 'wage_gross', 'wage_net']

