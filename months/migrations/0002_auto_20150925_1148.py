# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cash_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('cname', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='fixed_short_cost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('YM', models.TextField()),
                ('name', models.TextField()),
                ('cost', models.TextField()),
                ('cash_type', models.TextField()),
                ('end_date', models.TextField()),
                ('memo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='monthly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('YM', models.TextField()),
                ('cash', models.TextField()),
                ('total_cash', models.TextField()),
                ('credit', models.TextField()),
                ('total_credit', models.TextField()),
                ('cash_type', models.TextField()),
                ('memo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='other_cost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('YM', models.TextField()),
                ('name', models.TextField()),
                ('cost', models.TextField()),
                ('cash_type', models.TextField()),
                ('memo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='other_income',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('YM', models.TextField()),
                ('name', models.TextField()),
                ('cost', models.TextField()),
                ('memo', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='months',
            name='balance',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='months',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='months',
            name='invest_money',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='months',
            name='modify_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='months',
            name='total_balance',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='months',
            name='total_invest',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='months',
            name='total_invest2',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='months',
            name='YM',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='months',
            name='bonus',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='months',
            name='common_cost',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='months',
            name='parent_cost',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='months',
            name='salary',
            field=models.TextField(null=True, blank=True),
        ),
    ]
