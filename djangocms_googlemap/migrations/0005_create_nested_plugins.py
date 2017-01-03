# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def create_marker_and_route(apps, schema_editor):
    from cms import api
    from cms.models import Placeholder, CMSPlugin

    GoogleMap = apps.get_model('djangocms_googlemap', 'GoogleMap')
    plugins = GoogleMap.objects.all()

    for gmap in plugins:
        if (gmap.content or gmap.address or gmap.zipcode or gmap.city or
            gmap.lat or gmap.lng):
            placeholder = Placeholder.objects.get(pk=gmap.placeholder_id)
            target = CMSPlugin.objects.get(pk=gmap.pk)

            address = '{0}, {1}, {2}'.format(
                gmap.address, gmap.zipcode, gmap.city
            )

            # add nested marker plugin
            api.add_plugin(
                language=gmap.language,
                placeholder=placeholder,
                plugin_type='GoogleMapMarkerPlugin',
                position='last-child',
                target=target,
                # custom fields
                address=address,
                lat=gmap.lat,
                lng=gmap.lng,
                info_content=gmap.content,
            )

            if gmap.route_planer:
                # add nested route plugin
                api.add_plugin(
                    language=gmap.language,
                    placeholder=placeholder,
                    plugin_type='GoogleMapRoutePlugin',
                    position='last-child',
                    target=target,
                    # custom fields
                    title=gmap.route_planer_title or '',
                    destination=address,
                )


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_googlemap', '0004_adapted_fields'),
    ]

    operations = [
        migrations.RunPython(create_marker_and_route),
    ]
