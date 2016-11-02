# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_googlemap', '0005_create_nested_plugins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='googlemap',
            name='address',
        ),
        migrations.RemoveField(
            model_name='googlemap',
            name='city',
        ),
        migrations.RemoveField(
            model_name='googlemap',
            name='content',
        ),
        migrations.RemoveField(
            model_name='googlemap',
            name='zipcode',
        ),
        migrations.RemoveField(
            model_name='googlemap',
            name='route_planer',
        ),
        migrations.RemoveField(
            model_name='googlemap',
            name='route_planer_title',
        ),
        migrations.RemoveField(
            model_name='googlemap',
            name='info_window',
        ),
    ]
