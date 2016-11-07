# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_items', '0004_auto_20161103_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toolitem',
            name='categories',
            field=models.CharField(max_length=100, choices=[('WOODSHOP', 'Wood Shop'), ('FORGE', 'Forge'), ('3D', '3d Printing'), ('OTHER', 'Other'), ('CERAMICS', 'Ceramics'), ('Kitchen', 'Industrial Kitchen')], null=True, default='Other', blank=True),
        ),
    ]
