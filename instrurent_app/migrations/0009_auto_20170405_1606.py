# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrurent_app', '0008_auto_20170405_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='instrument_description',
            field=models.CharField(default=2000, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instrument',
            name='instrument_quantity',
            field=models.IntegerField(default=200),
        ),
    ]
