# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0015_auto_20150929_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthly',
            name='datetime',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='monthly',
            name='YM',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='monthly',
            name='cash',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='monthly',
            name='cash_type',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='monthly',
            name='credit',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='monthly',
            name='memo',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='monthly',
            name='total_cash',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='monthly',
            name='total_credit',
            field=models.TextField(null=True, blank=True),
        ),
    ]
