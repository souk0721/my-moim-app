# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('but_moim', '0007_auto_20160316_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw_info',
            name='withdraw_money',
            field=models.IntegerField(default=0),
        ),
    ]
