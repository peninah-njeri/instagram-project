# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-27 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0008_auto_20180727_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile'),
        ),
    ]
