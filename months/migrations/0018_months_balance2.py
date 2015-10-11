# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0017_auto_20150929_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='months',
            name='balance2',
            field=models.TextField(null=True, blank=True),
        ),
    ]
