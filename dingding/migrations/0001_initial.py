# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='分组', max_length=100)),
            ],
            options={
                'verbose_name': '分组',
                'verbose_name_plural': '分组管理',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.CharField(verbose_name='内容', max_length=200)),
                ('successful', models.CharField(verbose_name='成功', max_length=200)),
                ('failure', models.CharField(verbose_name='失败', max_length=200)),
            ],
            options={
                'verbose_name': '日志',
                'verbose_name_plural': '日志记录',
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=100)),
                ('num', models.CharField(verbose_name='工号', max_length=100, null=True, blank=True)),
                ('phone', models.CharField(verbose_name='电话', max_length=20, null=True, blank=True)),
                ('remark', models.CharField(verbose_name='备注', max_length=100, null=True, blank=True)),
                ('group', models.ManyToManyField(verbose_name='分组', to='dingding.Group')),
            ],
            options={
                'verbose_name': '人员',
                'verbose_name_plural': '人员管理',
                'ordering': ['num'],
            },
        ),
    ]
