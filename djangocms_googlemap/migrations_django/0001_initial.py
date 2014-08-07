# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleMap',
            fields=[
                ('title', models.CharField(max_length=100, null=True, verbose_name='map title', blank=True)),
                ('address', models.CharField(max_length=150, verbose_name='address')),
                ('zipcode', models.CharField(max_length=30, verbose_name='zip code')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('content', models.CharField(help_text='Displayed under address in the bubble.', max_length=255, verbose_name='additional content', blank=True)),
                ('zoom', models.PositiveSmallIntegerField(default=13, verbose_name='zoom level', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16'), (17, b'17'), (18, b'18'), (19, b'19'), (20, b'20'), (21, b'21')])),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10, blank=True, help_text='Use latitude & longitude to fine tune the map position.', null=True, verbose_name='latitude')),
                ('lng', models.DecimalField(null=True, verbose_name='longitude', max_digits=10, decimal_places=6, blank=True)),
                ('route_planer_title', models.CharField(default='Calculate your fastest way to here', max_length=150, null=True, verbose_name='route planer title', blank=True)),
                ('route_planer', models.BooleanField(default=False, verbose_name='route planer')),
                ('width', models.CharField(default=b'100%', help_text='Plugin width (in pixels or percent).', max_length=6, verbose_name='width')),
                ('height', models.CharField(default=b'400px', help_text='Plugin height (in pixels).', max_length=6, verbose_name='height')),
                ('info_window', models.BooleanField(default=True, help_text='Show textbox over marker', verbose_name='info window')),
                ('scrollwheel', models.BooleanField(default=True, help_text='Enable scrollwheel zooming on the map', verbose_name='scrollwheel')),
                ('double_click_zoom', models.BooleanField(default=True, verbose_name='double click zoom')),
                ('draggable', models.BooleanField(default=True, verbose_name='draggable')),
                ('keyboard_shortcuts', models.BooleanField(default=True, verbose_name='keyboard shortcuts')),
                ('pan_control', models.BooleanField(default=True, verbose_name='Pan control')),
                ('zoom_control', models.BooleanField(default=True, verbose_name='zoom control')),
                ('street_view_control', models.BooleanField(default=True, verbose_name='Street View control')),
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
