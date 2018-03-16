# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-09 10:54
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cerficates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='证书名称', max_length=30, unique=True, verbose_name='证书名称')),
                ('desc', models.TextField(default='', help_text='证书描述', verbose_name='证书描述')),
                ('score', models.IntegerField(default=1, help_text='证书得分', verbose_name='证书得分')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '证书',
                'verbose_name_plural': '证书',
            },
        ),
        migrations.CreateModel(
            name='IndexUserCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='certificates/images/', verbose_name='证书图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate_user', to='certificates.Cerficates', verbose_name='证书-用户')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_certificate', to=settings.AUTH_USER_MODEL, verbose_name='用户-证书')),
            ],
            options={
                'verbose_name': '用户-证书',
                'verbose_name_plural': '用户-证书',
            },
        ),
        migrations.AlterUniqueTogether(
            name='cerficates',
            unique_together=set([('name', 'score')]),
        ),
    ]
