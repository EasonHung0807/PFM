# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0022_remove_fixed_short_cost_ym'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixed_short_cost',
            name='level',
        ),
        migrations.RemoveField(
            model_name='fixed_short_cost1',
            name='level',
        ),
    ]
