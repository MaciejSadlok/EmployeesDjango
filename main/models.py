from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    hours = models.PositiveIntegerField()
    hourly_pay = models.PositiveIntegerField()
    wage_gross = models.PositiveIntegerField()
    wage_net = models.PositiveIntegerField()

    def __str__(self):
        return self.name + ' ' + self.surname


class DeletedEmployee(models.Model):
    employee_name = models.CharField(max_length=32)
    employee_surname = models.CharField(max_length=32)
    employee_hours = models.IntegerField(null=True, blank=True)
    employee_hourly_pay = models.IntegerField(null=True, blank=True)
    employee_wage_gross = models.IntegerField(null=True, blank=True)
    employee_wage_net = models.IntegerField(null=True, blank=True)








