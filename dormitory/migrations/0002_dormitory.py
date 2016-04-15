# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 00:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dormitory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dormitory',
            fields=[
                ('dor_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u5bbf\u820d\u7f16\u53f7')),
                ('name', models.IntegerField(verbose_name='\u5bbf\u820d\u540d')),
                ('capacity', models.IntegerField(verbose_name='\u5bb9\u91cf')),
                ('count', models.IntegerField(verbose_name='\u5df2\u7528\u7a7a\u95f4')),
                ('state', models.IntegerField(verbose_name='\u53ef\u7528\u72b6\u6001')),
                ('buil_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dormitory.building')),
            ],
        ),
    ]
