# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20150708_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='bannerImage',
            new_name='Imageurl',
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='bannerHeading',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='bannerText',
            new_name='headline',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 19, 55, 56, 227187), null=None, blank=None),
        ),
        migrations.AlterField(
            model_name='phone_design',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 19, 55, 56, 221674), null=None, blank=True),
        ),
        migrations.AlterField(
            model_name='selfi_image',
            name='selfi_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 19, 55, 56, 225263), null=None, blank=None),
        ),
    ]
