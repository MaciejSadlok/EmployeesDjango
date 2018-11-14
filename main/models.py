from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=32, verbose_name="Imię")
    surname = models.CharField(max_length=32, verbose_name="Nazwisko")
    hours = models.PositiveIntegerField(verbose_name="Ilość godzin")
    hourly_pay = models.PositiveIntegerField(verbose_name="Stawka godzinowa(PLN)")
    wage_gross = models.PositiveIntegerField(verbose_name="Suma brutto(PLN)")
    wage_net = models.PositiveIntegerField(verbose_name="Suma Netto(PLN)")

    def __str__(self):
        return self.name + ' ' + self.surname


class DeletedEmployee(models.Model):
    name = models.CharField(max_length=32, verbose_name="Imię")
    surname = models.CharField(max_length=32, verbose_name="Nazwisko")
    hours = models.IntegerField(verbose_name="Ilość godzin")
    hourly_pay = models.IntegerField(verbose_name="Stawka godzinowa(PLN)")
    wage_gross = models.IntegerField(verbose_name="Suma brutto(PLN)")
    wage_net = models.IntegerField(verbose_name="Suma netto(PLN)")








