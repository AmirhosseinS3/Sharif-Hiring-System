from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, Employer


class SignUpEmployerForm(UserCreationForm):
    name = forms.CharField(max_length=30, label='نام شرکت')
    email = forms.EmailField(max_length=254, label='ایمیل')
    address = forms.CharField(max_length=500, label='آدرس')
    description = forms.CharField(max_length=2000, label='توضیحات شرکت')
    password1 = forms.CharField(
        label='رمز عبور',
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput,
        strip=False,
        help_text='رمز عبور قبلی را دوباره وارد کنید',
    )

    def save(self, commit=True):
        user = super().save()
        name = self.cleaned_data['name']
        address = self.cleaned_data['address']
        description = self.cleaned_data['description']
        employer = Employer(name=name, address=address, description=description, username=user.id)
        employer.save()

    class Meta:
        model = Employer
        fields = ('name', 'address', 'email', 'description', 'password1', 'password2',)


class SignUpEmployeeForm(UserCreationForm):
    name = forms.CharField(max_length=30, label='نام و نام خانوادگی')
    email = forms.EmailField(max_length=254, label='ایمیل')
    password1 = forms.CharField(
        label='رمز عبور',
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput,
        strip=False,
        help_text='رمز عبور قبلی را دوباره وارد کنید',
    )

    class Meta:
        model = Employee
        fields = ('name', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save()
        name = self.cleaned_data['name']
        employer = Employee(name=name, username=user.username, email=user.email, password=user.password)
        employer.save()
