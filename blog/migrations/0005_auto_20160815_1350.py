# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160815_1259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='url_slug',
            field=models.SlugField(),
        ),
    ]
