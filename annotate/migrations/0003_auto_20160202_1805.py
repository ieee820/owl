# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0002_auto_20160202_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='annotation',
            name='log',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='annotate.Log'),
        ),
        migrations.AlterField(
            model_name='log',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
