# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrurent_app', '0006_auto_20170324_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='instrument_quantity',
            field=models.IntegerField(default=200),
        ),
    ]
