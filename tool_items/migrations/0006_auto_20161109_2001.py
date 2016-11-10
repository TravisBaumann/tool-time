# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_items', '0005_auto_20161104_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolitem',
            name='email',
            field=models.CharField(blank=True, max_length=40, default='No email contact', null=True),
        ),
        migrations.AddField(
            model_name='toolitem',
            name='phone',
            field=models.CharField(blank=True, max_length=15, default='No phone contact', null=True),
        ),
        migrations.AddField(
            model_name='toolitem',
            name='state',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='toolitem',
            name='zipcode',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='toolitem',
            name='categories',
            field=models.CharField(blank=True, max_length=100, choices=[('WOODSHOP', 'Wood Shop'), ('FORGE', 'Forge'), ('3D', '3d Printing'), ('OTHER', 'Other'), ('CERAMICS', 'Ceramics'), ('KITCHEN', 'Industrial Kitchen'), ('GLASSWORKING', 'Glassworking'), ('POTTERY', 'Pottery')], default='Other', null=True),
        ),
        migrations.AlterField(
            model_name='toolitem',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
