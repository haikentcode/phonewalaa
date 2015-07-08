# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150708_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogcode',
            field=models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blogname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 7, 42, 46, 980231), null=None, blank=None),
        ),
        migrations.AlterField(
            model_name='phone_design',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 7, 42, 46, 974531), null=None, blank=True),
        ),
        migrations.AlterField(
            model_name='selfi_image',
            name='selfi_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 7, 42, 46, 978085), null=None, blank=None),
        ),
    ]
