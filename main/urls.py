from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index/', views.main_page, name='main_page'),
    path('employees/', views.AllEmployees.as_view(), name='all_employees'),
    path('delete/<int:pk>', views.DeleteEmployee.as_view(), name='employee-delete')
]


