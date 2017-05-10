# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 04:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id_alt', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20)),
                ('drescription', models.CharField(max_length=255)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('show_date', models.DateField()),
                ('end_date', models.DateField()),
                ('active', models.IntegerField()),
                ('group', models.ManyToManyField(blank=True, to='auth.Group')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id_bus', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fax', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.CharField(max_length=255)),
                ('date_created', models.DateField()),
                ('active', models.IntegerField()),
                ('date_deactivated', models.DateField(blank=True, null=True)),
                ('messager', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id_cld', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id_cht', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('messager', models.CharField(max_length=255)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id_dir', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id_fil', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('drescription', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('date_save', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Folders',
            fields=[
                ('id_fld', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('folders_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Folders')),
            ],
        ),
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id_men', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.IntegerField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=45, null=True)),
                ('icon', models.CharField(max_length=20)),
                ('menus_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tools.Menus')),
            ],
        ),
        migrations.CreateModel(
            name='Menus_Group',
            fields=[
                ('id_mgr', models.AutoField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Menus')),
            ],
        ),
        migrations.AddField(
            model_name='files',
            name='folders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Folders'),
        ),
        migrations.AddField(
            model_name='files',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
