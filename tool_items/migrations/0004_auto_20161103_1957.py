# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_items', '0003_auto_20161028_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolitem',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='toolitem',
            name='categories',
            field=models.CharField(default='Other', max_length=100, null=True, choices=[('WOODSHOP', 'Wood Shop'), ('FORGE', 'Forge'), ('3D', '3d Printing'), ('OTHER', 'Other')], blank=True),
        ),
    ]
