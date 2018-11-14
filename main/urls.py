from django.urls import path
from main.models import Employee
from . import views
app_name = 'main'

urlpatterns = [
    path('index/', views.main_page, name='main-page'),
    path('employees/', views.employees, name='employees'),
    path('employees_delete/', views.delete_employee, name='employee-delete'),
    path('add_employee/', views.AddEmployee.as_view(model=Employee, success_url="/main/employees/"),
         name='add-employee'),
    path('deleted_employees/', views.deleted_employees, name='deleted-employees'),
    path('employees_hard_delete/', views.hard_delete_employee, name='hard_employee-delete'),

]


