# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20180725_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.TextField(max_length=50),
        ),
    ]
