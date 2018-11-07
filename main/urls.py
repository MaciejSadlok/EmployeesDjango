from django.urls import path
from main.models import Employee
from . import views
from django.urls import reverse

app_name = 'main'

urlpatterns = [
    path('index/', views.main_page, name='main-page'),
    path('employees/', views.custom_table, name='employees'),
    path('delete/', views.delete_employee, name='employee-delete'),
    path('add_employee/', views.AddEmployee.as_view(model=Employee, success_url="/main/employees/"),
         name='add-employee'),
    path('deleted_employees/', views.DeletedEmployeeTable.as_view(), name='deleted-employees')
]


