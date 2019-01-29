from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.hiring, name='hiring'),
    path(r'logout/', views.logout_user, name='logout'),
    path(r'about-us/', views.about_us, name='about_us'),
    path(r'blog_home/', views.blog_home, name='blog_home'),
    path(r'blog_single/', views.blog_single, name='blog_single'),
    path(r'category/', views.category, name='category'),
    path(r'contact/', views.contact, name='contact'),
    path(r'elements/', views.elements, name='elements'),
    path(r'index/', views.index, name='index'),
    path(r'login_employer/', views.login_employer, name='login_employer'),
    path(r'login_employee/', views.login_employee, name='login_employee'),
    path(r'price/', views.price, name='price'),
    path(r'single/', views.single, name='single'),
    path(r'user/', views.user, name='user'),
    path(r'sign_up_employer/', views.SignUpEmployer.as_view(), name='sign_up_employer'),
    path(r'sign_up_employee/', views.SignUpEmployee.as_view(), name='sign_up_employee'),
    path(r'success_signup/', views.success_signup, name='success_signup'),
    path(r'success_announcement/', views.success_announcement, name='success_announcement'),
    path(r'confirm_employee/<int:id>/<slug:code>/', views.confirm_employee, name='confirm_employee'),
    path(r'confirm_employer/<int:id>/<slug:code>/', views.confirm_employer, name='confirm_employer'),
    path(r'confirm_success/', views.confirm_success, name='confirm_success'),
    path(r'confirm_fail/', views.confirm_fail, name='confirm_fail'),
    path(r'create_announcement/<int:id>/', views.create_announcement, name='create_announcement'),
]

