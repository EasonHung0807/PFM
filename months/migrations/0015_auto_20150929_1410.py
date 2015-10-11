# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0014_auto_20150929_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invest',
            old_name='YM',
            new_name='datetime',
        ),
    ]
