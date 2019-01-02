from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.hiring, name='hiring'),
    path('about-us', views.about_us, name='about_us'),
    path('blog-home', views.blog_home, name='blog_home'),
    path('blog-single', views.blog_single, name='blog_single'),
    path('category', views.category, name='category'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('price', views.price, name='price'),
    path('single', views.single, name='single'),
    path('user', views.user, name='user'),
]