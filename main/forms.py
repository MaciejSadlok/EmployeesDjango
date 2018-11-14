from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=32, label="Nazwa użytkownika")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label='Adres e-mail')
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Hasło")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Powtórz hasło")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
