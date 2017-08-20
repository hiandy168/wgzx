# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('dingding', '0007_auto_20170817_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='num',
            new_name='member',
        ),
    ]
