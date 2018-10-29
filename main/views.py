from django.shortcuts import render
from .models import Employee
from django.views import View
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .filters import EmployeesFilter


class AllEmployees(ListView):
    model = Employee
    template_name = 'employees_table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EmployeesFilter(self.request.GET, queryset=self.get_queryset())
        return context


def main_page(request):
    return render(request, 'index.html')


class DeleteEmployee(DeleteView):
    model = Employee
    success_url = reverse_lazy('main:all_employees')





