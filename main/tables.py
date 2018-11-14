import django_tables2 as tables
from .models import Employee, DeletedEmployee


class EmployeeTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk')

    class Meta:
        model = Employee
        template = 'table_template.html'


class DeletedEmployeeTable(tables.Table):

    selection = tables.CheckBoxColumn(accessor='pk')

    class Meta:
        model = DeletedEmployee
        template = 'table_template.html'


