# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('but_moim', '0002_auto_20160314_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw_info',
            name='withdraw_date',
            field=models.CharField(max_length=100),
        ),
    ]
