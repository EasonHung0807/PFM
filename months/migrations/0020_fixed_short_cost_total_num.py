# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0019_auto_20151001_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixed_short_cost',
            name='total_num',
            field=models.TextField(null=True, blank=True),
        ),
    ]
