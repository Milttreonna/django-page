# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrurent_app', '0007_auto_20170324_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='instrument_quantity',
            field=models.IntegerField(max_length=200),
        ),
    ]