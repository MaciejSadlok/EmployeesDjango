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
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    hours = models.IntegerField(null=True, blank=True)
    hourly_pay = models.IntegerField(null=True, blank=True)
    wage_gross = models.IntegerField(null=True, blank=True)
    wage_net = models.IntegerField(null=True, blank=True)








