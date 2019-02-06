from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from hiring.models import Employer, Employee, Announcement, Comment, EmployeeComment
from .forms import SignUpEmployerForm, SignUpEmployeeForm, CreateAnnouncementForm, ResumeForm, \
    CommentForm, EditEmployeeProfileForm, EmployeeCommentForm


def hiring(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about-us.html')


def blog_home(request):
    return render(request, 'blog-home.html')


class SignUpEmployer(generic.CreateView):
    form_class = SignUpEmployerForm
    success_url = '/hiring/success_signup/'
    template_name = 'sign-up-employer.html'

    def get_success_url(self):
        return self.success_url


class SignUpEmployee(generic.CreateView):
    form_class = SignUpEmployeeForm
    success_url = '/hiring/success_signup/'
    template_name = 'sign-up-employee.html'

    def get_success_url(self):
        return self.success_url


@login_required
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
                request.session['username'] = username
                request.session['id'] = Employee.objects.get(username=username).id
                request.session['isEmployee'] = True
                return redirect('/hiring/user')
                # return HttpResponseRedirect('/hiring/user')


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
                request.session['username'] = username
                request.session['id'] = Employer.objects.get(username=username).id
                request.session['isEmployee'] = False
                return redirect('/hiring/user')
                # return HttpResponseRedirect('/hiring/user')


def price(request):
    return render(request, 'price.html')


def single(request):
    return render(request, 'single-post.html')


@login_required
def user(request):
    username = request.session['username']
    id = request.session['id']
    isEmployee = request.session['isEmployee']
    return render(request, 'user.html', {'username': username, 'isEmployee': isEmployee, 'id': id})


@login_required
def success_announcement(request):
    return render(request, 'success_announcement.html')


def confirm_success(request):
    return render(request, 'confirm_success.html')


def confirm_fail(request):
    return render(request, 'confirm_fail.html')


# class CreateAnnouncement(generic.CreateView):
#     form_class = CreateAnnouncementForm
#     success_url = 'hiring/success_announcement/'
#     template_name = 'create-announcement.html'

@login_required
def create_announcement(request, id):
    if request.method == 'GET':
        form = CreateAnnouncementForm()
        return render(request, 'create-announcement.html', {'form': form})
    elif request.method == 'POST':
        form = CreateAnnouncementForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            announce = Announcement(title=data['title'], category=data['category'],
                                    employer=Employer.objects.get(id=id))
            announce.save()
            print('good')
            return HttpResponseRedirect('/hiring/success_announcement')


@login_required
def logout_user(requet):
    logout(requet)
    return HttpResponseRedirect('/hiring')


@login_required
def announcements(request, id):
    username = request.session['username']
    id = request.session['id']
    isEmployee = request.session['isEmployee']
    announcements = Announcement.objects.all()
    return render(request, 'user.html',
                  {'username': username, 'isEmployee': isEmployee, 'id': id, 'announcements': announcements})


def confirm_employee(request, id, code):
    if request.method == 'GET':
        employee = Employee.objects.get(id=id)
        actual_code = employee.confirmation_code
        if code == actual_code:
            employee.activated = True
            employee.save()
            return HttpResponseRedirect('/hiring/confirm_success/')
        else:
            return HttpResponseRedirect('/hiring/confirm_failed/')


def confirm_employer(request, id, code):
    if request.method == 'GET':
        employer = Employer.objects.get(id=id)
        actual_code = employer.confirmation_code
        if code == actual_code:
            employer.activated = True
            employer.save()
            return HttpResponseRedirect('/hiring/confirm_success')
        else:
            return HttpResponseRedirect('/hiring/confirm_failed')


def success_signup(request):
    return render(request, 'success_signup.html')


def success_comment(request):
    return render(request, 'success_comment.html')


@login_required()
def success_edit_profile(request):
    return render(request, 'success_edit_profile.html')


@login_required
def success_announcement(request):
    return render(request, 'success_announcement.html')


def success_upload_resume(request):
    return render(request, 'success_upload_resume.html')


# class CreateAnnouncement(generic.CreateView):
#     form_class = CreateAnnouncementForm
#     success_url = 'hiring/success_announcement/'
#     template_name = 'create-announcement.html'

@login_required
def create_announcement(request, id):
    if request.method == 'GET':
        form = CreateAnnouncementForm()
        return render(request, 'create-announcement.html', {'form': form})
    elif request.method == 'POST':
        form = CreateAnnouncementForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            announce = Announcement(title=data['title'], category=data['category'], employer=Employer.objects.get(id=id))
            announce.save()
            print('good')
            return HttpResponseRedirect('/hiring/success_announcement')


@login_required
def logout_user(requet):
    logout(requet)
    return HttpResponseRedirect('/hiring')


@login_required
def announcements(request, id):
    emp = Employer.objects.filter(id=id).first()
    announcements = Announcement.objects.filter(employer=emp).filter(is_allowed=True)
    name = emp.name
    address = emp.address
    desc = emp.description
    id = id
    return render(request, 'announcements.html', {'announcements': announcements, 'id': id, 'name': name,
                                                  'address': address, 'description': desc})


@login_required
def edit_profile_employee(request, id):
    employee = Employee.objects.filter(id=id).first()
    if request.method == 'GET':
        form = EditEmployeeProfileForm(instance=employee)
        return render(request, 'edit-profile.html', {'form': form, 'id': id})
    elif request.method == 'POST':
        form = EditEmployeeProfileForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/hiring/success_edit_profile')
        else:
            return render(request, 'edit-profile.html', {'form': form, 'id': id})


@login_required
def upload_resume(request, id):
    employee = Employee.objects.filter(id=id).first()
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # data = form.cleaned_data
            # resume = Resume(document= data['document'])
            # form.save()
            employee.resume = form.save()
            employee.save()
            # form.save()
            return HttpResponseRedirect('/hiring/success_upload_resume')
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {
        'form': form
    })


@login_required
def announcement(request, id):
    announcement = Announcement.objects.filter(id=id).first()
    comments = Comment.objects.filter(announcement_id=id)
    return render(request, 'single-post.html', {'announcement': announcement, 'comments': comments})


@login_required
def announcement_comment(request, id):
    employee_username = request.session['username']
    employee = Employee.objects.filter(username=employee_username).first()
    employee_id = employee.id
    announcement = Announcement.objects.filter(id=id).first()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.announcement = announcement
            comment.employee = employee
            comment.save()
            return redirect('/hiring/success_comment')
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form, 'id': employee.id})


@login_required
def employee_page(request, id):
    employee = Employee.objects.filter(id=id).first()
    comments = EmployeeComment.objects.filter(employee_id=id)
    return render(request, 'employee-page.html', {'employee': employee, 'comments': comments})


@login_required
def employee_comment(request, id):
    print(id)
    employer_username = request.session['username']
    employer = Employer.objects.filter(username=employer_username).first()
    employee = Employee.objects.filter(id=id).first()
    if request.method == "POST":
        form = EmployeeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.employer = employer
            comment.employee = employee
            comment.save()
            return redirect('/hiring/success_comment')
    else:
        form = EmployeeCommentForm()
    return render(request, 'employee-comment.html', {'form': form, 'id': employer.id})