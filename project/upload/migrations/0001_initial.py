# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-25 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import project.upload.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='', validators=[project.upload.validators.validate_file_extension])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Document')),
            ],
        ),
    ]
