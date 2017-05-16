# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_auto_20170511_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdescrip',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='fee',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='invoiceshasitems',
            name='value_ind',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]