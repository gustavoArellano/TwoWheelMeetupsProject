# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-06 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0018_auto_20190605_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='UsersGoing',
            field=models.ManyToManyField(related_name='UsersGoingRelated', to='MainApp.User'),
        ),
    ]
