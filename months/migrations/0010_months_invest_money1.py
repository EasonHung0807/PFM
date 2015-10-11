# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0009_months_phone_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='months',
            name='invest_money1',
            field=models.TextField(null=True, blank=True),
        ),
    ]
