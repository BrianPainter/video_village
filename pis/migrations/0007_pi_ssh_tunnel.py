# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-22 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0006_pi_cpu_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pi',
            name='ssh_tunnel',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
