# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0020_fixed_short_cost_total_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixed_short_cost',
            name='rent_cost',
        ),
        migrations.RemoveField(
            model_name='fixed_short_cost',
            name='rent_num',
        ),
    ]
