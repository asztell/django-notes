# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-07 00:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20170305_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 7, 0, 2, 6, 376956, tzinfo=utc)),
        ),
    ]