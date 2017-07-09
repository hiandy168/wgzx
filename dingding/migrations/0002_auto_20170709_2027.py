# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dingding', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='failure',
            new_name='fail',
        ),
        migrations.RenameField(
            model_name='log',
            old_name='successful',
            new_name='success',
        ),
    ]
