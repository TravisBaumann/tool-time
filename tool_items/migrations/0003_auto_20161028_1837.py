# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_items', '0002_auto_20161028_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toolitem',
            name='categories',
            field=models.CharField(max_length=100, null=True, default='Other', blank=True, choices=[('WOODSHOP', 'Wood Shop'), ('FORGE', 'Forge'), ('3D', '3d Printing'), ('OTHER', 'OTHER')]),
        ),
    ]
