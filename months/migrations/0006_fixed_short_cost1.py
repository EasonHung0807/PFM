# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0005_auto_20150927_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='fixed_short_cost1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('YM', models.TextField(null=True, blank=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('cost', models.TextField(null=True, blank=True)),
                ('short_costid', models.TextField(null=True, blank=True)),
                ('memo', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
                ('level', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
