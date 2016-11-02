# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_googlemap', '0007_reset_null_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlemap',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Map title', blank=True),
            preserve_default=False,
        ),
    ]
