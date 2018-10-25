from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('employees/', views.all_employees, name='all_employees'),
    path('delete/<int:pk>', views.DeleteEmployee.as_view(), name='employee-delete')

]