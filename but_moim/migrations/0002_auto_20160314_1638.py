# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('but_moim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notice_title', models.CharField(max_length=100)),
                ('notice_textarea', models.TextField(max_length=2000, blank=True)),
                ('notice_date', models.CharField(max_length=100, null=True, blank=True)),
                ('notice_date_day', models.CharField(default=datetime.datetime.now, max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='deposit_amount',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='deposit_date',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='deposit_yse_no',
        ),
        migrations.AddField(
            model_name='deposit_info',
            name='account_yse_no',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deposit_info',
            name='deposit_date_Day',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='moim_info',
            name='deposit_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='moim_info',
            name='moim_total_money2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_info',
            name='user_pk',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deposit_info',
            name='deposit_amount',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='deposit_info',
            name='deposit_date',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='deposit_info',
            name='user_name',
            field=models.ForeignKey(to='but_moim.user_info2'),
        ),
        migrations.AlterField(
            model_name='withdraw_info',
            name='withdraw_date',
            field=models.CharField(max_length=110),
        ),
        migrations.AddField(
            model_name='notice',
            name='moim_name',
            field=models.ForeignKey(to='but_moim.moim_info'),
        ),
        migrations.AddField(
            model_name='notice',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
