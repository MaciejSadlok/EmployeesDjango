from django.forms import ModelForm
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'surname', 'hours', 'hourly_pay', 'wage_gross', 'wage_net']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)