# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dingding', '0002_auto_20170709_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='author',
            field=models.CharField(verbose_name='操作', max_length=200, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.DateTimeField(verbose_name='时间', max_length=200),
        ),
    ]
