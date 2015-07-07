# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blogcode', models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True)),
                ('blogname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='blogpost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postCode', models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True)),
                ('headLine', models.CharField(max_length=200)),
                ('postData', models.TextField(max_length=5000)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 7, 6, 17, 31, 24, 464478), null=None, blank=None)),
                ('postStatus', models.CharField(default=b'show', max_length=10)),
                ('postImage', models.ImageField(upload_to=b'media/blog')),
                ('blog', models.ForeignKey(to='home.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Create_Own_Design',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('design_Image', models.ImageField(upload_to=b'media/create_own_design')),
                ('phone_Company', models.TextField(max_length=20)),
                ('phone_Model', models.TextField(max_length=20)),
                ('email_Id', models.TextField(max_length=50)),
                ('design_Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemType', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('offer_image', models.ImageField(upload_to=b'./temp')),
                ('offer_code', models.CharField(max_length=100)),
                ('cover_count', models.IntegerField(null=True, blank=True)),
                ('offer_count', models.IntegerField(null=True, blank=True)),
                ('time_start', models.DateField()),
                ('time_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone_Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100)),
                ('company_logo', models.ImageField(upload_to=b'media/company_logo')),
            ],
        ),
        migrations.CreateModel(
            name='Phone_Design',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('design_code', models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True)),
                ('design_Image', models.ImageField(upload_to=b'media/design_image')),
                ('design_name', models.CharField(max_length=100)),
                ('desing_specification', models.CharField(max_length=500)),
                ('design_status', models.CharField(max_length=10)),
                ('design_sell_count', models.IntegerField(null=True, blank=True)),
                ('design_hit_count', models.IntegerField(null=True, blank=True)),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2015, 7, 6, 17, 31, 24, 460027), null=None, blank=True)),
                ('design_price', models.IntegerField(default=100)),
                ('design_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Phone_Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_name', models.CharField(max_length=100)),
                ('model_code', models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True)),
                ('model_company', models.ForeignKey(to='home.Phone_Company')),
            ],
        ),
        migrations.CreateModel(
            name='Selfi_Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('selfi_code', models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True)),
                ('selfi_image', models.ImageField(upload_to=b'media/selfi')),
                ('selfi_time', models.DateTimeField(default=datetime.datetime(2015, 7, 6, 17, 31, 24, 462893), null=None, blank=None)),
                ('selfi_status', models.CharField(default=b'no', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullName', models.TextField(max_length=100)),
                ('addressLine_1', models.TextField(max_length=200)),
                ('addressLine_2', models.TextField(max_length=200)),
                ('town', models.TextField(max_length=20)),
                ('stateName', models.TextField(max_length=50)),
                ('pinCode', models.IntegerField()),
                ('countaryName', models.TextField(max_length=20)),
                ('mobileNo', models.TextField(max_length=15)),
                ('additionalAddress', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('emailId', models.EmailField(max_length=254, serialize=False, primary_key=True)),
                ('contactNo', models.CharField(max_length=10)),
                ('cityName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('dateOfBirth', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='user',
            field=models.ForeignKey(to='home.User'),
        ),
        migrations.AddField(
            model_name='selfi_image',
            name='selfi_user',
            field=models.ForeignKey(to='home.User'),
        ),
        migrations.AddField(
            model_name='phone_design',
            name='design_model',
            field=models.ForeignKey(to='home.Phone_Model'),
        ),
        migrations.AddField(
            model_name='item',
            name='itemCompany',
            field=models.ForeignKey(to='home.Phone_Company'),
        ),
    ]
