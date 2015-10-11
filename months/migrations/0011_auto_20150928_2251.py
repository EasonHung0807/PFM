# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0010_months_invest_money1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='months',
            old_name='invest_money1',
            new_name='invest_grow',
        ),
    ]
