# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0018_months_balance2'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixed_short_cost1',
            name='rent_cost',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fixed_short_cost1',
            name='rent_num',
            field=models.TextField(null=True, blank=True),
        ),
    ]
