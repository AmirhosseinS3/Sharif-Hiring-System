from django.contrib.auth.models import User
from django.db import models


class Resume(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Employee(User):
    name = models.CharField(max_length=30, null=False)
    confirmation_code = models.CharField(max_length=6)
    activated = models.BooleanField(default=False)
    skills = models.CharField(max_length=200, default='None')
    city = models.CharField(max_length=40, default='Tehran')
    experience = models.CharField(max_length=200, default='None')
    description = models.CharField(max_length=200, default='None')
    MAJORS = (
        ('CoE', 'مهندسی کامپیوتر'),
        ('ElE', 'مهندسی برق'),
        ('MeE', 'مهندسی مکانیک'),
        ('MaE', 'مهندسی مواد'),
        ('ChE', 'مهندسی شیمی'),
        ('IE', 'مهندسی صنایع'),
        ('CiE', 'مهندسی عمران'),
    )
    major = models.CharField(max_length=50, choices=MAJORS)
    isAlumni = models.BooleanField(default=False)
    resume = models.ForeignKey(Resume, on_delete='SET_NULL', related_name='employee', null=True, blank=True)
    #num_of_scores = models.IntegerField(default=0)
    #num_of_comments = models.IntegerField(default=0)
    #sum_of_scores = models.FloatField(default=0.)


class Employer(User):
    name = models.CharField(max_length=30, null=False, primary_key=True)
    address = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=2000, null=False)
    confirmation_code = models.CharField(max_length=6)
    activated = models.BooleanField(default=False)
    #num_of_scores = models.IntegerField(default=0)
    #num_of_comments = models.IntegerField(default=0)
    #sum_of_scores = models.FloatField(default=0.)


class Announcement(models.Model):
    title = models.CharField(max_length=30)
    JOB_CATEGORIES = (
        ('CoE', 'مهندسی کامپیوتر'),
        ('ElE', 'مهندسی برق'),
        ('MeE', 'مهندسی مکانیک'),
        ('MaE', 'مهندسی مواد'),
        ('ChE', 'مهندسی شیمی'),
        ('IE', 'مهندسی صنایع'),
        ('CiE', 'مهندسی عمران'),
    )
    category = models.CharField(max_length=50, choices=JOB_CATEGORIES)
    CONTRACT_TYPES = (
        ('FT', 'تمام وقت'),
        ('PT', 'پاره وقت'),
    )
    contract_type = models.CharField(max_length=10, choices=CONTRACT_TYPES)
    salary_range_start = models.IntegerField(default=0)
    salary_range_limit = models.IntegerField(default=100000)
    city = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    applicants = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    employer = models.ForeignKey(to=Employer, on_delete=models.CASCADE)
    is_allowed = models.BooleanField(default=False)


class Comment(models.Model):
    announcement = models.ForeignKey(to=Announcement, on_delete=models.CASCADE, related_name='comments')
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class EmployeeComment(models.Model):
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, related_name='comments_employee')
    employer = models.ForeignKey(to=Employer, on_delete=models.CASCADE, related_name='comments_employer')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
