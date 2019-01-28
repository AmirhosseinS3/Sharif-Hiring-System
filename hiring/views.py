from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from hiring.models import Employer, Employee
from .forms import SignUpEmployerForm, SignUpEmployeeForm


def hiring(request):
    return render(request, 'login_employee.html')


def about_us(request):
    return render(request, 'about-us.html')


def blog_home(request):
    return render(request, 'blog-home.html')


class SignUpEmployer(generic.CreateView):
    form_class = SignUpEmployerForm
    success_url = 'hiring/success/'
    template_name = 'sign-up-employer.html'


class SignUpEmployee(generic.CreateView):
    form_class = SignUpEmployeeForm
    success_url = 'hiring/success/'
    template_name = 'sign-up-employee.html'


def blog_single(request):
    return render(request, 'single-post.html')


def category(request):
    return render(request, 'category.html')


def contact(request):
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def index(request):
    return render(request, 'index.html')


def login_employee(request):
    if request.method == 'GET':
        return render(request, 'login_employee.html')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        employee = Employee.objects.filter(email=email)
        if not employee:
            return render(request, 'login_employee.html', {'errors': 'ایمیل در سیستم وجود ندارد'})
        else:
            username = employee[0].username
            employee = authenticate(request, username=username, password=password)
            if employee is None:
                return render(request, 'login_employee.html', {'errors': 'رمز عبور اشتباه'})
            else:
                login(request, employee)
                return HttpResponseRedirect('/hiring/user')


def login_employer(request):
    if request.method == 'GET':
        return render(request, 'login_employer.html')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        employer = Employer.objects.filter(email=email)
        if not employer:
            return render(request, 'login_employer.html', {'errors': 'ایمیل در سیستم وجود ندارد'})
        else:
            username = employer[0].username
            employer = authenticate(request, username=username, password=password)
            if employer is None:
                return render(request, 'login_employer.html', {'errors': 'رمز عبور اشتباه'})
            else:
                login(request, employer)
                return HttpResponseRedirect('/hiring/user')


def price(request):
    return render(request, 'price.html')


def single(request):
    return render(request, 'single-post.html')


def user(request):
    return render(request, 'user.html')


def confirm_employee(reques):
    if request.method == 'POST':
        entered_code = request.POST['code']
        id = request.POST['id']
        employee = Employee.objects.get(id=id)
        actual_code = employee.confirmation_code
        if entered_code == actual_code:
            employee.activated = True
            employee.save()
            return HttpResponseRedirect('hiring/confirm_success')
        else:
            return HttpResponseRedirect('hiring/confirm_failed')


def confirm_employer(request):
    if request.method == 'POST':
        entered_code = request.POST['code']
        id = request.POST['id']
        employer = Employer.objects.get(id=id)
        actual_code = employer.confirmation_code
        if entered_code == actual_code:
            employer.activated = True
            employer.save()
            return HttpResponseRedirect('hiring/confirm_success')
        else:
            return HttpResponseRedirect('hiring/confirm_failed')


def success(request):
    return render(request, 'success.html')


def confirm_success(request):
    return render(request, 'confirm_success.html')


def confirm_fail(request):
    return render(request, 'confirm_fail.html')
