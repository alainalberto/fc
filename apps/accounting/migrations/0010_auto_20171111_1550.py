# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0009_auto_20170830_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='ach_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='comition_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='wire_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='overtime_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='pay_date',
            field=models.DateField(blank=True, default='2017-11-11', null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='regular_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='start_date',
            field=models.DateField(default='2017-11-11'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='start_date',
            field=models.DateField(default='2017-11-11'),
        ),
    ]
