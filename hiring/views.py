from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpEmployerForm


def hiring(request):
    return render(request, 'login.html')


def about_us(request):
    return render(request, 'about-us.html')


def blog_home(request):
    return render(request, 'blog-home.html')


class SignUpEmployer(generic.CreateView):
    form_class = SignUpEmployerForm
    success_url = reverse_lazy('login_employer')
    template_name = 'sign-up-employer.html'


class SignUpEmployee(generic.CreateView):
    form_class = SignUpEmployeeForm
    success_url = reverse_lazy('login_employee')
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


def login(request):
    return render(request, 'login.html')


def price(request):
    return render(request, 'price.html')


def single(request):
    return render(request, 'single-post.html')


def user(request):
    return render(request, 'user.html')
