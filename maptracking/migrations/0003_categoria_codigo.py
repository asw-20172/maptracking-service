# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maptracking', '0002_auto_20171003_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='codigo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
