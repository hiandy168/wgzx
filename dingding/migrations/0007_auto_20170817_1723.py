# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dingding', '0006_auto_20170817_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='fail',
            field=models.CharField(verbose_name='失败', max_length=200, default=1),
            preserve_default=False,
        ),
    ]
