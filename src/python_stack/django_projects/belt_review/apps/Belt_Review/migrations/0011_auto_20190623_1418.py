# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-23 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Belt_Review', '0010_auto_20190623_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='creator',
            field=models.CharField(max_length=60),
        ),
    ]