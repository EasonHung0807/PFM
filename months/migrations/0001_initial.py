# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Months',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('YM', models.TextField()),
                ('salary', models.TextField()),
                ('bonus', models.TextField()),
                ('parent_cost', models.TextField()),
                ('common_cost', models.TextField()),
            ],
        ),
    ]
