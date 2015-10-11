# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0007_fixed_short_cost_rent_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='months',
            name='balance1',
            field=models.TextField(null=True, blank=True),
        ),
    ]
