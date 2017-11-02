# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCalorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.CharField(max_length=200, verbose_name='内容')),
                ('image_addr', models.URLField(verbose_name='链接')),
            ],
        ),
    ]
