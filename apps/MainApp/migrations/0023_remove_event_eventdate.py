# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-01 00:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0022_event_eventdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='EventDate',
        ),
    ]
