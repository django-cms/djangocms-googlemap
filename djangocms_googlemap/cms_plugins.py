# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


GOOGLEMAP_API_KEY = getattr(
    settings,
    'DJANGOCMS_GOOGLEMAP_API_KEY',
    None,
)


class GoogleMapPlugin(CMSPluginBase):
    model = models.GoogleMap
    name = _('Google Map')
    admin_preview = False
    allow_children = True
    child_classes = ['GoogleMapMarkerPlugin', 'GoogleMapRoutePlugin']

    fieldsets = [
        (None, {
            'fields': (
                'title',
                ('width', 'height',),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'template',
                ('lat', 'lng',),
                'style',
            )
        }),
        (_('Control settings'), {
            'classes': ('collapse',),
            'fields': (
                ('zoom', 'map_type_control',),
                ('zoom_control', 'double_click_zoom',),
                ('street_view_control', 'draggable',),
                ('rotate_control', 'keyboard_shortcuts',),
                ('scale_control', 'scrollwheel',),
                'fullscreen_control',
                'pan_control',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_googlemap/{}/map.html'.format(instance.template)

    def render(self, context, instance, placeholder):
        context = super(GoogleMapPlugin, self).render(context, instance, placeholder)
        context['googlemap_template'] = instance.template
        context['googlemap_key'] = GOOGLEMAP_API_KEY
        return context


class GoogleMapMarkerPlugin(CMSPluginBase):
    model = models.GoogleMapMarker
    name = _('Marker')
    module = _('Google Map')
    require_parent = True
    parent_classes = ['GoogleMapPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'title',
                'address',
                ('lat', 'lng',),
                'icon',
            )
        }),
        (_('Info window'), {
            'classes': ('collapse',),
            'fields': (
                'show_content',
                'info_content',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_googlemap/{}/marker.html'.format(context['googlemap_template'])


class GoogleMapRoutePlugin(CMSPluginBase):
    model = models.GoogleMapRoute
    name = _('Route')
    module = _('Google Map')
    require_parent = True
    parent_classes = ['GoogleMapPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'title',
                ('origin', 'destination',),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'travel_mode',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_googlemap/{}/route.html'.format(context['googlemap_template'])


plugin_pool.register_plugin(GoogleMapPlugin)
plugin_pool.register_plugin(GoogleMapMarkerPlugin)
plugin_pool.register_plugin(GoogleMapRoutePlugin)
