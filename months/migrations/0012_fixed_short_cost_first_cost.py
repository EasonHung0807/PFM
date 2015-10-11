# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0011_auto_20150928_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixed_short_cost',
            name='first_cost',
            field=models.TextField(null=True, blank=True),
        ),
    ]
