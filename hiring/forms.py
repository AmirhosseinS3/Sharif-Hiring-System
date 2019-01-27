from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpEmployerForm(UserCreationForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    address = forms.CharField(max_length=500)
    description = forms.CharField(max_length=2000)

    class Meta:
        model = Employer
        fields = ('name', 'address', 'email', 'description', 'password1', 'password2',)


class SignUpEmployeeForm(UserCreationForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Employee
        fields = ('name', 'email', 'password1', 'password2',)
