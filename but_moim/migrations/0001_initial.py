# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='deposit_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deposit_date', models.DateField()),
                ('deposit_amount', models.IntegerField(default=40000)),
                ('deposit_yse_no', models.BooleanField(default=False)),
                ('deposit_name', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='moim_info',
            fields=[
                ('moim_name', models.CharField(unique=True, max_length=100)),
                ('moim_deposit_date', models.CharField(max_length=100)),
                ('moim_account_name', models.CharField(max_length=100)),
                ('moim_account_bank', models.CharField(max_length=100)),
                ('moim_account_num', models.CharField(max_length=100)),
                ('moim_total_money', models.IntegerField(default=0)),
                ('moim_code', models.AutoField(serialize=False, primary_key=True)),
                ('moim_symbol', models.ImageField(upload_to=b'', blank=True)),
                ('moim_person_count', models.IntegerField(default=1)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='outstanding_amount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('out_standing_amount', models.IntegerField()),
                ('moim_name', models.ForeignKey(to='but_moim.moim_info')),
            ],
        ),
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.CharField(max_length=100, null=True, blank=True)),
                ('manager', models.BooleanField(default=False)),
                ('user_name', models.CharField(max_length=100)),
                ('deposit_date', models.DateField()),
                ('deposit_amount', models.IntegerField(default=40000)),
                ('deposit_yse_no', models.BooleanField(default=False)),
                ('moim_name', models.ForeignKey(to='but_moim.moim_info')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_info2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.CharField(max_length=100, null=True, blank=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='withdraw_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('withdraw_date', models.DateField()),
                ('withdraw_amount', models.IntegerField()),
                ('withdraw_title', models.CharField(max_length=100)),
                ('receipt_img', models.ImageField(upload_to=b'', blank=True)),
                ('moim_name', models.ForeignKey(to='but_moim.moim_info')),
            ],
        ),
        migrations.AddField(
            model_name='outstanding_amount',
            name='user_name',
            field=models.ForeignKey(to='but_moim.user_info'),
        ),
        migrations.AddField(
            model_name='deposit_info',
            name='moim_name',
            field=models.ForeignKey(to='but_moim.moim_info'),
        ),
        migrations.AddField(
            model_name='deposit_info',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deposit_info',
            name='user_name',
            field=models.ForeignKey(to='but_moim.user_info'),
        ),
    ]
