# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def add_plugin(apps, plugin_type, plugin_model, language, placeholder, parent, **data):
    from cms.models import CMSPlugin
    from treebeard.mp_tree import MP_AddChildHandler

    # This is a CMSPlugin instance which represents the model's
    # current state for the current migration
    plugin = apps.get_model('cms', 'CMSPlugin')(
        parent=parent,
        placeholder=placeholder,
        language=language,
        plugin_type=plugin_type,
        position=(parent.cmsplugin_set.count() + 1),
    )

    # This is a CMSPlugin instance which represents the current
    # state of the model class itself, does not respect migrations.
    # Needed because of the treebeard operations that rely on internal methods
    concrete_parent = (
        CMSPlugin
        .objects
        .only('numchild', 'depth', 'path')
        .get(pk=parent.pk)
    )

    MP_AddChildHandler(concrete_parent, instance=plugin).process()

    bound_plugin = plugin_model(**data)
    bound_plugin.cmsplugin_ptr = plugin

    for attr in ('parent_id', 'placeholder', 'language', 'plugin_type', 'creation_date', 'depth', 'path',
                 'numchild', 'pk', 'position'):
        setattr(bound_plugin, attr, getattr(plugin, attr))
    bound_plugin.save()
    return bound_plugin


def create_marker_and_route(apps, schema_editor):
    Placeholder = apps.get_model('cms', 'Placeholder')
    CMSPlugin = apps.get_model('cms', 'CMSPlugin')
    GoogleMap = apps.get_model('djangocms_googlemap', 'GoogleMap')
    GoogleMapMarker = apps.get_model('djangocms_googlemap', 'GoogleMapMarker')
    GoogleMapRoute = apps.get_model('djangocms_googlemap', 'GoogleMapRoute')

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
            add_plugin(
                apps=apps,
                plugin_type='GoogleMapMarkerPlugin',
                plugin_model=GoogleMapMarker,
                language=gmap.language,
                placeholder=placeholder,
                parent=target,
                # custom fields
                address=address,
                lat=gmap.lat,
                lng=gmap.lng,
                info_content=gmap.content,
            )

            if gmap.route_planer:
                # add nested route plugin
                add_plugin(
                    apps=apps,
                    plugin_type='GoogleMapRoutePlugin',
                    plugin_model=GoogleMapRoute,
                    language=gmap.language,
                    placeholder=placeholder,
                    parent=target,
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
