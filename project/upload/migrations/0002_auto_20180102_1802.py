# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='message',
            field=models.TextField(),
        ),
    ]
