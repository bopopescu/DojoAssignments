# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-13 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='User',
        ),
    ]
