# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0021_auto_20151002_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixed_short_cost',
            name='YM',
        ),
    ]
