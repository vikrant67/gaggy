# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 18:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gag', '0008_auto_20170417_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='upload_date',
            field=models.TimeField(blank=True, default=datetime.datetime(2017, 4, 17, 18, 1, 37, 215494, tzinfo=utc)),
        ),
    ]