# Generated by Django 2.1.1 on 2018-11-06 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181103_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deletedemployee',
            old_name='employee_hourly_pay',
            new_name='hourly_pay',
        ),
        migrations.RenameField(
            model_name='deletedemployee',
            old_name='employee_hours',
            new_name='hours',
        ),
        migrations.RenameField(
            model_name='deletedemployee',
            old_name='employee_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='deletedemployee',
            old_name='employee_surname',
            new_name='surname',
        ),
        migrations.RenameField(
            model_name='deletedemployee',
            old_name='employee_wage_gross',
            new_name='wage_gross',
        ),
        migrations.RenameField(
            model_name='deletedemployee',
            old_name='employee_wage_net',
            new_name='wage_net',
        ),
    ]