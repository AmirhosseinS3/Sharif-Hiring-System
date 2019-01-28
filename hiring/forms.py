from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string

from .models import Employee, Employer


class SignUpEmployerForm(UserCreationForm):
    name = forms.CharField(max_length=30, label='نام شرکت')
    username = forms.CharField(max_length=30, label='نام کاربری')
    email = forms.EmailField(max_length=254, label='ایمیل')
    address = forms.CharField(max_length=500, label='آدرس')
    description = forms.CharField(max_length=2000, label='توضیحات شرکت')
    password1 = forms.CharField(
        label='رمز عبور',
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput,
        strip=False,
    )

    def save(self, commit=True):
        employer = super().save()
        unique_code = get_random_string(length=6)
        employer.confirmation_code = unique_code
        employer.save()
        email_message = EmailMessage('Confirm your account!',
                                     'hiring/confirm_employer/' + str(employer.id) + '/' + str(unique_code), '',
                                     [self.cleaned_data['email']])
        email_message.send()

    class Meta:
        model = Employer
        fields = ('name', 'username', 'address', 'email', 'description', 'password1', 'password2',)


class SignUpEmployeeForm(UserCreationForm):
    name = forms.CharField(max_length=30, label='نام و نام خانوادگی')
    email = forms.EmailField(max_length=254, label='ایمیل')
    username = forms.CharField(label='شماره ملی')
    password1 = forms.CharField(
        label='رمز عبور',
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput,
        strip=False,
    )

    def save(self, commit=True):
        employee = super().save()
        unique_code = get_random_string(length=6)
        employee.confirmation_code = unique_code
        employee.save()
        email_message = EmailMessage('Confirm your account!',
                                     'hiring/confirm_employee/' + str(employee.id) + '/' + str(unique_code), '',
                                     [self.cleaned_data['email']])
        email_message.send()

    class Meta:
        model = Employee
        fields = ('name', 'username', 'email', 'password1', 'password2',)
