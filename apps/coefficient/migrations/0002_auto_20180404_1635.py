# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-04 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coefficient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coefficientdetail',
            name='coefficent',
            field=models.DecimalField(decimal_places=2, default=0, help_text='系数', max_digits=4, verbose_name='系数'),
        ),
    ]
