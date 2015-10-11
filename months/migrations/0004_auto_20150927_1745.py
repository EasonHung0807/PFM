# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0003_auto_20150925_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixed_short_cost',
            name='start_date',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fixed_short_cost',
            name='cash_type',
            field=models.TextField(null=True, blank=True),
        ),
    ]
