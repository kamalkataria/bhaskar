# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfoods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=100)),
                ('user_message', models.TextField()),
                ('active_or_disable', models.CharField(blank=True, choices=[('ACTIVE', 'active'), ('DISABLED', 'disabled')], default='DISABLED', max_length=15, null=True)),
            ],
        ),
    ]
