from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm


def hiring(request):
    return render(request, 'login.html')


def about_us(request):
    return render(request, 'about-us.html')


def blog_home(request):
    return render(request, 'blog-home.html')


class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login_employer')
    template_name = 'signup.html'


def sign_up_employer(request):
    return render(request, 'sign-up-employer.html')


def sign_up_employee(request):
    return render(request, 'sign-up-employee.html')


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
