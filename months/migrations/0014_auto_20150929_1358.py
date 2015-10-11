# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0013_invest_invest_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='invest',
            name='rest',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='invest',
            name='total',
            field=models.TextField(null=True, blank=True),
        ),
    ]
