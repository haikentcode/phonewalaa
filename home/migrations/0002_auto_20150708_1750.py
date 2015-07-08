# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 17, 50, 37, 234843), null=None, blank=None),
        ),
        migrations.AlterField(
            model_name='phone_design',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 17, 50, 37, 230300), null=None, blank=True),
        ),
        migrations.AlterField(
            model_name='selfi_image',
            name='selfi_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 17, 50, 37, 233209), null=None, blank=None),
        ),
    ]
