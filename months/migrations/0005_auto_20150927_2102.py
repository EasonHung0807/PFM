# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0004_auto_20150927_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixed_short_cost',
            name='level',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fixed_short_cost',
            name='YM',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fixed_short_cost',
            name='cost',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fixed_short_cost',
            name='end_date',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fixed_short_cost',
            name='memo',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fixed_short_cost',
            name='name',
            field=models.TextField(null=True, blank=True),
        ),
    ]
