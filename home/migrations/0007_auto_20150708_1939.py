# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150708_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 19, 39, 36, 17184), null=None, blank=None),
        ),
        migrations.AlterField(
            model_name='phone_design',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 19, 39, 36, 11428), null=None, blank=True),
        ),
        migrations.AlterField(
            model_name='selfi_image',
            name='selfi_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 19, 39, 36, 15168), null=None, blank=None),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='additionalAddress',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='addressLine_1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='addressLine_2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='countaryName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='fullName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='mobileNo',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='stateName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='town',
            field=models.CharField(max_length=20),
        ),
    ]
