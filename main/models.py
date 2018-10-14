from django.db import models


class Employee(models.Model):
    employee_name = models.CharField(max_length=32)
    employee_surname = models.CharField(max_length=32)
    employee_hours = models.IntegerField()
    employee_hourly_pay = models.FloatField()
    employee_wage_gross = models.FloatField()
    employee_wage_net = models.FloatField()





