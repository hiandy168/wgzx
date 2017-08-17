# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dingding', '0004_auto_20170817_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='success',
        ),
        migrations.AddField(
            model_name='log',
            name='num',
            field=models.CharField(verbose_name='总数', max_length=200, default=1),
            preserve_default=False,
        ),
    ]
