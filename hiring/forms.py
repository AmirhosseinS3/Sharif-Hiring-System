from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, EmailMessage
from django.forms import ModelForm, BaseModelForm
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string

from .models import Employee, Employer, Announcement


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


class CreateAnnouncementForm(ModelForm):
    title = forms.CharField(max_length=30, label='عنوان شغل')
    JOB_CATEGORIES = (
        ('CoE', 'مهندسی کامپیوتر'),
        ('ElE', 'مهندسی برق'),
        ('MeE', 'مهندسی مکانیک'),
        ('MaE', 'مهندسی مواد'),
        ('ChE', 'مهندسی شیمی'),
        ('IE', 'مهندسی صنایع'),
        ('CiE', 'مهندسی عمران'),
    )
    category = forms.ChoiceField(choices=JOB_CATEGORIES, label='دسته بندی شغل')
    CONTRACT_TYPES = (
        ('FT', 'تمام وقت'),
        ('PT', 'پاره وقت'),
    )
    contract_type = forms.ChoiceField(choices=CONTRACT_TYPES, label='نوع قرارداد')
    salary_range_start = forms.IntegerField(label='حداقل دستمزد')
    salary_range_limit = forms.IntegerField(label='حداکثر دستمزد')
    city = forms.CharField(max_length=40, label='شهر')
    description = forms.CharField(max_length=200, label='توضیحات')
    applicants = forms.CharField(max_length=200, label='به چگونه افرادی نیاز دارید')
    experience = forms.CharField(max_length=200, label='تجربه های موردنیاز')

    class Meta:
        model = Announcement
        fields = ['title', 'category', 'contract_type', 'salary_range_start',
                  'salary_range_limit', 'city', 'description', 'applicants',
                  'experience']
