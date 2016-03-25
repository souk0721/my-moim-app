# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('but_moim', '0003_auto_20160314_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='user_pk',
        ),
    ]
