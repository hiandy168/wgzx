# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dingding', '0003_auto_20170817_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.CharField(verbose_name='时间', max_length=200),
        ),
    ]
