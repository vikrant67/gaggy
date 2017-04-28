# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 14:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gag', '0002_auto_20170320_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='upload',
            name='upload_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
