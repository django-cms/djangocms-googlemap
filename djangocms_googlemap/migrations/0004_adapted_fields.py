# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

from djangocms_googlemap.models import get_templates


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_googlemap', '0003_auto_20160825_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='googlemap',
            name='fullscreen_control',
            field=models.BooleanField(default=True, help_text='Allows the user to select a fullscreen view of the map.', verbose_name='Enable fullscreen mode'),
        ),
        migrations.AddField(
            model_name='googlemap',
            name='map_type_control',
            field=models.CharField(default='ROADMAP', max_length=255, verbose_name='Map type', choices=[('ROADMAP', 'ROADMAP'), ('SATELLITE', 'SATELLITE'), ('HYBRID', 'HYBRID'), ('TERRAIN', 'TERRAIN')]),
        ),
        migrations.AddField(
            model_name='googlemap',
            name='rotate_control',
            field=models.BooleanField(default=True, help_text='Allows the user to change the orientation of the map.', verbose_name='Enable rotation'),
        ),
        migrations.AddField(
            model_name='googlemap',
            name='scale_control',
            field=models.BooleanField(default=True, help_text='Displays a linear distance scale on the map.', verbose_name='Enable map scale'),
        ),
        migrations.AddField(
            model_name='googlemap',
            name='template',
            field=models.CharField(default=get_templates()[0][0], max_length=255, verbose_name='Template', choices=get_templates()),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='djangocms_googlemap_googlemap', primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Address', blank=True),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='city',
            field=models.CharField(max_length=255, verbose_name='City', blank=True),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='content',
            field=models.CharField(help_text='Displayed under address in the bubble.', max_length=255, verbose_name='Additional content', blank=True),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='double_click_zoom',
            field=models.BooleanField(default=True, help_text='Allows the user to zoom and centre the map with a double-click or double-tap.', verbose_name='Enable double-click zoom'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='draggable',
            field=models.BooleanField(default=True, help_text='Allows the user to drag the map to see new areas.', verbose_name='Enable dragging'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='height',
            field=models.CharField(default='400px', help_text='Height of the map, including the CSS length units (e.g. "400px" or "400rem").', max_length=6, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='info_window',
            field=models.BooleanField(default=True, help_text='Show textbox over marker', verbose_name='Info window'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='keyboard_shortcuts',
            field=models.BooleanField(default=True, help_text='Allows the user to control the map using the keyboard.', verbose_name='Enable keyboard shortcuts'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='lat',
            field=models.FloatField(help_text='Default Geographical latitude in degrees (e.g. "46.947973").', verbose_name='Latitude (lat)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='lng',
            field=models.FloatField(help_text='Default Geographical longitude in degrees (e.g. "7.447446").', verbose_name='Longitude (lng)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='route_planer',
            field=models.BooleanField(default=False, verbose_name='Enable route planner'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='route_planer_title',
            field=models.CharField(default='Calculate your fastest way to here', max_length=150, null=True, verbose_name='Route planner title', blank=True),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='scrollwheel',
            field=models.BooleanField(default=True, help_text='Allows the user to control the zoom level with a scroll-wheel.', verbose_name='Enable scroll-wheel zooming'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='street_view_control',
            field=models.BooleanField(default=True, help_text='Street View allows the user to see street-level imagery.', verbose_name='Enable Street View'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='style',
            field=models.TextField(help_text='Provide a valid (escaped) JSON configuration. See http://developers.google.com/maps/documentation/javascript/styling', verbose_name='Map styling', blank=True),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Map title', blank=True),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='width',
            field=models.CharField(default='100%', help_text='Width of the map, including the CSS length units (e.g. "100%", "400px" or "400rem").', max_length=6, verbose_name='Width'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='zipcode',
            field=models.CharField(max_length=255, verbose_name='ZIP code', blank=True),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='zoom',
            field=models.PositiveSmallIntegerField(default=13, verbose_name='Zoom level', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21')]),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='zoom_control',
            field=models.BooleanField(default=True, help_text='Enabling zooming allows the user to view the map at different scales.', verbose_name='Enable zooming'),
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='pan_control',
            field=models.BooleanField(default=True, help_text='Allows the user to move the map using the cursor keys to see new areas.', verbose_name='Enable cursor key panning'),
        ),
        migrations.CreateModel(
            name='GoogleMapMarker',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_googlemap_googlemapmarker', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=django.db.models.deletion.CASCADE)),
                ('title', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('address', models.CharField(max_length=255, verbose_name='Full address', blank=True, help_text='Note: Latitude and longitude can be used to fine-tune the location.')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10, blank=True, help_text='Geographical latitude in degrees (e.g. "46.947973").', null=True, verbose_name='Latitude (lat)')),
                ('lng', models.DecimalField(decimal_places=6, max_digits=10, blank=True, help_text='Geographical longitude in degrees (e.g. "7.447446").', null=True, verbose_name='Longitude (lng)')),
                ('show_content', models.BooleanField(default=True, verbose_name='Show window', help_text='Display the info window when the map loads.')),
                ('info_content', models.TextField(help_text='Will be displayed in the info window attached to the marker.', verbose_name='Info window content', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GoogleMapRoute',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_googlemap_googlemaproute', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=django.db.models.deletion.CASCADE)),
                ('title', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('origin', models.CharField(max_length=255, verbose_name='Starting address', blank=True, help_text='Will be determined by user\'s location (if possible) if left blank.')),
                ('destination', models.CharField(max_length=255, verbose_name='Destination address')),
                ('travel_mode', models.CharField(max_length=255, verbose_name='Travel mode', choices=[('DRIVING', 'DRIVING'), ('BICYCLING', 'BICYCLING'), ('TRANSIT', 'TRANSIT'), ('WALKING', 'WALKING')], default='DRIVING')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
