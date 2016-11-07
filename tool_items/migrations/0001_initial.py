# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(null=True, max_digits=6, default=1.0, blank=True, decimal_places=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('categories', models.CharField(null=True, choices=[('WOODSHOP', 'Wood Shop'), ('PRODUCE', 'Wood Shop'), ('DAIRY', 'Dairy'), ('BAKERY', 'Bread/Bakery')], max_length=100, default='Other', blank=True)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
