# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-08 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_auto_20170708_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='winnings',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
