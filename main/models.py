from django.db import models


class Employee(models.Model):
    employee_name = models.CharField(max_length=32)
    employee_surname = models.CharField(max_length=32)
    employee_hours = models.IntegerField(null=True, blank=True)
    employee_hourly_pay = models.IntegerField(null=True, blank=True)
    employee_wage_gross = models.IntegerField(null=True, blank=True)
    employee_wage_net = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.employee_name + ' ' + self.employee_surname


class DeletedEmployee(models.Model):
    employee_name = models.CharField(max_length=32)
    employee_surname = models.CharField(max_length=32)
    employee_hours = models.IntegerField(null=True, blank=True)
    employee_hourly_pay = models.IntegerField(null=True, blank=True)
    employee_wage_gross = models.IntegerField(null=True, blank=True)
    employee_wage_net = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.employee_name + ' ' + self.employee_surname






