# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(upload_to='posts/'),
        ),
    ]