# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote_date', models.DateField()),
                ('quote_description', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuoteDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote_detail_description', models.CharField(max_length=200)),
                ('quantity', models.DecimalField(max_digits=5, decimal_places=2)),
                ('unit_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quote', models.ForeignKey(to='wrenchmarks_app.Quote')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuotePart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote_part_description', models.CharField(max_length=200)),
                ('quantity', models.DecimalField(max_digits=5, decimal_places=2)),
                ('unit_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quote', models.ForeignKey(to='wrenchmarks_app.Quote')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_date', models.DateField()),
                ('service_description', models.CharField(max_length=80)),
                ('service_mileage', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceEventDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detail_description', models.CharField(max_length=200)),
                ('technician', models.CharField(max_length=30)),
                ('work_order', models.CharField(max_length=20)),
                ('quantity', models.DecimalField(max_digits=5, decimal_places=2)),
                ('unit_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('service_event', models.ForeignKey(to='wrenchmarks_app.ServiceEvent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceEventPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_description', models.CharField(max_length=200)),
                ('technician', models.CharField(max_length=30)),
                ('work_order', models.CharField(max_length=20)),
                ('quantity', models.DecimalField(max_digits=5, decimal_places=2)),
                ('unit_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('service_event', models.ForeignKey(to='wrenchmarks_app.ServiceEvent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_model', models.CharField(max_length=30)),
                ('vehicle_make', models.CharField(max_length=30)),
                ('vehicle_year', models.CharField(max_length=4)),
                ('colour', models.CharField(max_length=20)),
                ('plate', models.CharField(max_length=12)),
                ('VIN', models.CharField(max_length=17)),
                ('mileage', models.IntegerField()),
                ('customer', models.ForeignKey(to='wrenchmarks_app.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='serviceevent',
            name='vehicle',
            field=models.ForeignKey(to='wrenchmarks_app.Vehicle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quote',
            name='vehicle',
            field=models.ForeignKey(to='wrenchmarks_app.Vehicle'),
            preserve_default=True,
        ),
    ]
