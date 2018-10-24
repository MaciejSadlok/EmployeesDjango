from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.all_employees)

]