# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-18 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_publisher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]