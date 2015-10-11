# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0012_fixed_short_cost_first_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='invest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('YM', models.TextField(null=True, blank=True)),
                ('invest_type', models.TextField(null=True, blank=True)),
                ('cash', models.TextField(null=True, blank=True)),
                ('memo', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='invest_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('cname', models.TextField(null=True, blank=True)),
                ('pn', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
