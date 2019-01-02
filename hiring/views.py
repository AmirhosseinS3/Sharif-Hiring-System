from django.shortcuts import render


def hiring(request):
    return render(request, 'login.html')


def about_us(request):
    return render(request, 'about-us.html')


def blog_home(request):
    return render(request, 'blog-home.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def category(request):
    return render(request, 'category.html')


def contact(request):
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def employer(request):
    return render(request, 'employer.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def price(request):
    return render(request, 'price.html')


def search(request):
    return render(request, 'search.html')


def single(request):
    return render(request, 'single.html')


def user(request):
    return render(request, 'user.html')
