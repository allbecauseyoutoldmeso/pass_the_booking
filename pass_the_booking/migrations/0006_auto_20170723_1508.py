# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pass_the_booking', '0005_remove_booking_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
