# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gag', '0003_auto_20170411_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='hy', max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='upload',
            name='id',
        ),
        migrations.AddField(
            model_name='upload',
            name='comment_id',
            field=models.CharField(default=0, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gag.Upload'),
        ),
    ]