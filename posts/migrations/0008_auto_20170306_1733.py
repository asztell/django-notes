# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-07 01:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170306_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 3, 7, 1, 33, 17, 638118, tzinfo=utc)),
        ),
    ]
