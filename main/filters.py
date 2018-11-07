import django_filters
from .models import Employee, DeletedEmployee


class EmployeesFilter(django_filters.FilterSet):

    class Meta:
        model = Employee
        fields = ['name', 'surname']
