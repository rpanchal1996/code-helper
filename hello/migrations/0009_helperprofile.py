# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-20 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='helperProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('personal_details', models.CharField(max_length=400)),
                ('github_link', models.CharField(max_length=100)),
            ],
        ),
    ]