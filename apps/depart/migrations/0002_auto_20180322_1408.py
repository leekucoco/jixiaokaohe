# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-22 14:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('depart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='indexuserdepart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_depart', to=settings.AUTH_USER_MODEL, verbose_name='用户-部门'),
        ),
        migrations.AddField(
            model_name='departdetail',
            name='leader',
            field=models.ForeignKey(help_text='主管领导', on_delete=django.db.models.deletion.CASCADE, related_name='dept_leader', to=settings.AUTH_USER_MODEL, verbose_name='主管领导'),
        ),
        migrations.AddField(
            model_name='departdetail',
            name='manager',
            field=models.ForeignKey(help_text='部门经理', on_delete=django.db.models.deletion.CASCADE, related_name='dept_manager', to=settings.AUTH_USER_MODEL, verbose_name='部门经理'),
        ),
        migrations.AddField(
            model_name='departdetail',
            name='parent_dept',
            field=models.ForeignKey(blank=True, help_text='上级部门', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentdept', to='depart.DepartDetail', verbose_name='上级部门'),
        ),
        migrations.AlterUniqueTogether(
            name='indexuserdepart',
            unique_together=set([('user', 'depart')]),
        ),
    ]