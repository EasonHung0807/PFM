# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0008_months_balance1'),
    ]

    operations = [
        migrations.AddField(
            model_name='months',
            name='phone_cost',
            field=models.TextField(null=True, blank=True),
        ),
    ]
