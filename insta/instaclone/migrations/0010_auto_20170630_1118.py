# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-30 11:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0009_auto_20170630_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 30, 11, 18, 36, 495855)),
        ),
    ]