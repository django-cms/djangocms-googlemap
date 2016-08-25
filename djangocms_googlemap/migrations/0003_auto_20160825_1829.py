# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_googlemap', '0002_auto_20160622_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlemap',
            name='style',
            field=models.TextField(help_text='Provide a valid JSON configuration (escaped). See developers.google.com/maps/documentation/javascript/styling', verbose_name='custom map style', blank=True),
        ),
    ]
