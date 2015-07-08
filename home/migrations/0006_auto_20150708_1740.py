# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20150708_0742'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bannerImage', models.ImageField(upload_to=b'media/banner')),
                ('bannerText', models.CharField(max_length=100)),
                ('bannerHeading', models.CharField(max_length=100)),
                ('bannerStatus', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 17, 40, 55, 342320), null=None, blank=None),
        ),
        migrations.AlterField(
            model_name='phone_design',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 17, 40, 55, 336796), null=None, blank=True),
        ),
        migrations.AlterField(
            model_name='selfi_image',
            name='selfi_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 17, 40, 55, 340281), null=None, blank=None),
        ),
    ]
