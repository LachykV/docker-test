from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, label="FIRSTNAME",
        widget=forms.TextInput(attrs={'class': 'form-control input', 'id': 'first_name'})
    )
    last_name = forms.CharField(
        max_length=30, required=True, label="LASTNAME",
        widget=forms.TextInput(attrs={'class': 'form-control input', 'id': 'last_name'})
    )
    middle_name = forms.CharField(
        max_length=30, required=False, label="MIDDLENAME",
        widget=forms.TextInput(attrs={'class': 'form-control input', 'id': 'middle_name'})
    )
    email = forms.EmailField(
        max_length=254, required=True, label="EMAIL",
        widget=forms.EmailInput(attrs={'class': 'form-control input', 'id': 'email'})
    )
    password1 = forms.CharField(
        label="PASSWORD",
        widget=forms.PasswordInput(attrs={'class': 'form-control input', 'id': 'password1'})
    )
    password2 = forms.CharField(
        label="CONFIRM PASSWORD",
        widget=forms.PasswordInput(attrs={'class': 'form-control input', 'id': 'password2'})
    )

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "middle_name", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control input', 'id': 'username'}),
        label="USERNAME"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control input', 'id': 'password'}),
        label="PASSWORD"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']