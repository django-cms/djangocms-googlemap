# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleMap',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, to='cms.CMSPlugin', primary_key=True, on_delete=django.db.models.deletion.CASCADE)),
                ('title', models.CharField(verbose_name='map title', blank=True, null=True, max_length=100)),
                ('address', models.CharField(verbose_name='address', max_length=150)),
                ('zipcode', models.CharField(verbose_name='zip code', max_length=30)),
                ('city', models.CharField(verbose_name='city', max_length=100)),
                ('content', models.CharField(help_text='Displayed under address in the bubble.', blank=True, max_length=255, verbose_name='additional content')),
                ('zoom', models.PositiveSmallIntegerField(verbose_name='zoom level', default=13, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21')])),
                ('lat', models.DecimalField(help_text='Use latitude & longitude to fine tune the map position.', blank=True, max_digits=10, verbose_name='latitude', null=True, decimal_places=6)),
                ('lng', models.DecimalField(max_digits=10, verbose_name='longitude', blank=True, null=True, decimal_places=6)),
                ('route_planer_title', models.CharField(verbose_name='route planer title', blank=True, null=True, max_length=150, default='Calculate your fastest way to here')),
                ('route_planer', models.BooleanField(verbose_name='route planer', default=False)),
                ('width', models.CharField(help_text='Plugin width (in pixels or percent).', default='100%', max_length=6, verbose_name='width')),
                ('height', models.CharField(help_text='Plugin height (in pixels).', default='400px', max_length=6, verbose_name='height')),
                ('info_window', models.BooleanField(help_text='Show textbox over marker', default=True, verbose_name='info window')),
                ('scrollwheel', models.BooleanField(help_text='Enable scrollwheel zooming on the map', default=True, verbose_name='scrollwheel')),
                ('double_click_zoom', models.BooleanField(verbose_name='double click zoom', default=True)),
                ('draggable', models.BooleanField(verbose_name='draggable', default=True)),
                ('keyboard_shortcuts', models.BooleanField(verbose_name='keyboard shortcuts', default=True)),
                ('pan_control', models.BooleanField(verbose_name='Pan control', default=True)),
                ('zoom_control', models.BooleanField(verbose_name='zoom control', default=True)),
                ('street_view_control', models.BooleanField(verbose_name='Street View control', default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
