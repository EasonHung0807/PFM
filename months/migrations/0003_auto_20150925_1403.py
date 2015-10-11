# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0002_auto_20150925_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixed_short_cost',
            name='rent_cost',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fixed_short_cost',
            name='total_cost',
            field=models.TextField(null=True, blank=True),
        ),
    ]
