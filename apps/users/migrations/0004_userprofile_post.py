# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-12 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180312_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='post',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='岗位'),
        ),
    ]
