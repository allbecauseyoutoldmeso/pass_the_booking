# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('mobile', models.CharField(max_length=200)),
            ],
        ),
    ]