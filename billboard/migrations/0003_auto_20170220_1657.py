# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-20 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0002_auto_20170220_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=b'empty title', max_length=100, null=True),
        ),
    ]
