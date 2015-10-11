# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0016_auto_20150929_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invest',
            name='rest',
        ),
        migrations.RemoveField(
            model_name='invest',
            name='total',
        ),
        migrations.RemoveField(
            model_name='months',
            name='total_invest2',
        ),
    ]
