# Generated by Django 2.1.4 on 2019-02-01 09:51

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('CoE', 'مهندسی کامپیوتر'), ('ElE', 'مهندسی برق'), ('MeE', 'مهندسی مکانیک'), ('MaE', 'مهندسی مواد'), ('ChE', 'مهندسی شیمی'), ('IE', 'مهندسی صنایع'), ('CiE', 'مهندسی عمران')], max_length=50)),
                ('contract_type', models.CharField(choices=[('FT', 'تمام وقت'), ('PT', 'پاره وقت')], max_length=10)),
                ('salary_range_start', models.IntegerField(default=0)),
                ('salary_range_limit', models.IntegerField(default=100000)),
                ('city', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('applicants', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200)),
                ('is_allowed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=30)),
                ('confirmation_code', models.CharField(max_length=6)),
                ('activated', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
                ('confirmation_code', models.CharField(max_length=6)),
                ('activated', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='announcement',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiring.Employer'),
        ),
    ]
