# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-03 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_auto_20190522_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='UserGoing',
            field=models.ManyToManyField(related_name='UserGoing', to='MainApp.User'),
        ),
    ]