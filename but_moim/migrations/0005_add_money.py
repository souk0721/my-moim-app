# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('but_moim', '0004_remove_user_info_user_pk'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_money',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_money', models.IntegerField(default=0, max_length=10)),
                ('add_money_title', models.CharField(max_length=100)),
                ('add_money_textarea', models.TextField(max_length=2000, blank=True)),
                ('add_money_date', models.CharField(max_length=100, null=True, blank=True)),
                ('add_money_date_day', models.CharField(default=datetime.datetime.now, max_length=100, null=True, blank=True)),
                ('moim_name', models.ForeignKey(to='but_moim.moim_info')),
            ],
        ),
    ]
