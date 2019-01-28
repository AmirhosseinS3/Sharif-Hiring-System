from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .models import Employee, Employer


class SignUpEmployerForm(UserCreationForm):
    name = forms.CharField(max_length=30, label='نام شرکت')
    username = forms.CharField(max_length=30, label='نام کاربری')
    email = forms.EmailField(max_length=254, label='ایمیل')
    address = forms.CharField(max_length=500, label='آدرس')
    description = forms.CharField(max_length=2000, label='توضیحات شرکت')

    # def __init__(self):
    #     super().__init__()
    #     self.password1.label = 'رمز عبور'
    #     self.password2.label = 'تکرار رمز عبور'

    def save(self, commit=True):
        employer = super().save()
        unique_id = get_random_string(length=6)
        employer.confirmation_code = unique_id
        employer.save()
        send_mail('Confirm your account!', unique_id, '', [self.cleaned_data['email']])

    class Meta:
        model = Employer
        fields = ('name', 'username', 'address', 'email', 'description', 'password1', 'password2',)


class SignUpEmployeeForm(UserCreationForm):
    name = forms.CharField(max_length=30, label='نام و نام خانوادگی')
    email = forms.EmailField(max_length=254, label='ایمیل')
    username = forms.CharField(label='شماره ملی')

    # def __init__(self):
    #     super().__init__()
    #     self.password1.label = 'رمز عبور'
    #     self.password2.label = 'تکرار رمز عبور'

    def save(self, commit=True):
        employee = super().save()
        unique_id = get_random_string(length=6)
        employee.confirmation_code = unique_id
        employee.save()
        send_mail('Confirm your account!', unique_id, '', [self.cleaned_data['email']])
        # employer = Employee.objects.get(username=self.cleaned_data['username'])
        # employer.confirmation_code = unique_id
        # send_mail('Confirm your account!', unique_id, '', self.cleaned_data['email'])

    class Meta:
        model = Employee
        fields = ('name', 'username', 'email', 'password1', 'password2',)
