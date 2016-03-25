# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('but_moim', '0005_add_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_money',
            name='add_money',
            field=models.IntegerField(default=0),
        ),
    ]
