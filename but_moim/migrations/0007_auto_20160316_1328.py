# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('but_moim', '0006_auto_20160315_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdraw_info',
            old_name='withdraw_amount',
            new_name='withdraw_money',
        ),
        migrations.AddField(
            model_name='withdraw_info',
            name='withdraw_date_day',
            field=models.CharField(default=datetime.datetime.now, max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='withdraw_info',
            name='withdraw_textarea',
            field=models.TextField(max_length=2000, blank=True),
        ),
    ]
