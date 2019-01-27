from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.hiring, name='hiring'),
    path('about-us', views.about_us, name='about_us'),
    path('blog_home', views.blog_home, name='blog_home'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('category', views.category, name='category'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('index', views.index, name='index'),
    path('login_employer', views.login_employer, name='login_employer'),
    path('login_employee', views.login_employee, name='login_employee'),
    path('price', views.price, name='price'),
    path('single', views.single, name='single'),
    path('user', views.user, name='user'),
    path('sign_up_employer', views.SignUpEmployer.as_view, name='sign_up_employer'),
    path('sign_up_employee', views.SignUpEmployee.as_view, name='sign_up_employee'),
]

