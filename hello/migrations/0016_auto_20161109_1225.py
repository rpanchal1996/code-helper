# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-09 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0015_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='created_at',
        ),
        migrations.AddField(
            model_name='message',
            name='curr_time',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]