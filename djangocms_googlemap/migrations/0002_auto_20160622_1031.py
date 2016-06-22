# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_googlemap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='googlemap',
            name='style',
            field=models.TextField(help_text='Use javascript as in', verbose_name='custom map style', blank=True),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='djangocms_googlemap_googlemap', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='route_planer',
            field=models.BooleanField(default=False, verbose_name='route planner'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='route_planer_title',
            field=models.CharField(default='Calculate your fastest way to here', max_length=150, null=True, verbose_name='route planner title', blank=True),
        ),
    ]
