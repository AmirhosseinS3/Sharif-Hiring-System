# Generated by Django 2.1.4 on 2019-02-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring', '0004_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='upload_by',
        ),
        migrations.AddField(
            model_name='employee',
            name='Resume',
            field=models.ForeignKey(default=None, on_delete='SET_NULL', related_name='employee', to='hiring.Resume'),
        ),
    ]