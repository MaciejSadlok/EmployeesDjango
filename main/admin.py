from django.contrib import admin
from .models import Employee, DeletedEmployee


admin.site.register(Employee)
admin.site.register(DeletedEmployee)

