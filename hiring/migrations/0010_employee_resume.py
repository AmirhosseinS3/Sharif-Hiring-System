# Generated by Django 2.1.4 on 2019-02-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring', '0009_remove_employee_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Resume',
            field=models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', related_name='employee', to='hiring.Resume'),
        ),
    ]
