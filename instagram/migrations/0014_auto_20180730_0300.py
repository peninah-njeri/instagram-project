# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0013_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.TextField(),
        ),
    ]
