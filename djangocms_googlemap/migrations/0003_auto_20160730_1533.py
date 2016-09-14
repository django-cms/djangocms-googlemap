# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('cms', '0016_auto_20160608_1535'),
        ('djangocms_googlemap', '0002_auto_20160622_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleMapLocation',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='cms.CMSPlugin', primary_key=True, related_name='djangocms_googlemap_googlemaplocation')),
                ('title', models.CharField(max_length=100, blank=True, null=True, verbose_name='map title')),
                ('address', models.CharField(max_length=150, verbose_name='address')),
                ('zipcode', models.CharField(max_length=30, verbose_name='zip code')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('content', models.CharField(max_length=255, blank=True, help_text='Displayed under address in the bubble.', verbose_name='additional content')),
                ('lat', models.DecimalField(null=True, help_text='Use latitude & longitude to fine tune the map position.', verbose_name='latitude', max_digits=10, blank=True, decimal_places=6)),
                ('lng', models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name='longitude')),
                ('info_window', models.BooleanField(default=True, help_text='Show textbox over marker', verbose_name='info window')),
                ('marker_icon', filer.fields.file.FilerFileField(null=True, help_text='Map marker icon. Leave empty for the default red Google Map pin.', to='filer.File', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
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
            name='info_window',
        ),
        migrations.RemoveField(
            model_name='googlemap',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='googlemap',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='googlemap',
            name='title',
        ),
        migrations.RemoveField(
            model_name='googlemap',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='googlemap',
            name='style',
            field=models.TextField(blank=True, help_text='Provide a valid JSON configuration (escaped). See developers.google.com/maps/documentation/javascript/styling', verbose_name='custom map style'),
        ),
    ]
