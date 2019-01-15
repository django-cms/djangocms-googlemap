# -*- coding: utf-8 -*-
"""
Enables the user to add various google maps plugin that adds maps or images
from the google maps api.
"""
from __future__ import unicode_literals

import json
import re

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from filer.fields.image import FilerImageField

MAP_TYPES = ['ROADMAP', 'SATELLITE', 'HYBRID', 'TERRAIN']
MAP_TYPE_CHOICES = [(map_type, map_type) for map_type in MAP_TYPES]
TRAVEL_MODES = ['DRIVING', 'BICYCLING', 'TRANSIT', 'WALKING']
TRAVEL_MODE_CHOICES = [(travel_mode, travel_mode) for travel_mode in TRAVEL_MODES]
ZOOM_LEVEL_CHOICES = [(c, str(c)) for c in range(22)]  # from 0 to 21

CSS_WIDTH_RE = re.compile(r'^\d+(?:px|%)$')
CSS_HEIGHT_RE = re.compile(r'^\d+px$')


# Add additional choices through the ``settings.py``.
def get_templates():
    choices = [
        ('default', _('Default')),
    ]
    choices += getattr(
        settings,
        'DJANGOCMS_GOOGLEMAP_TEMPLATES',
        [],
    )
    return choices


@python_2_unicode_compatible
class GoogleMap(CMSPlugin):
    """
    Renders the Google Maps wrapper
    """
    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=255,
    )
    title = models.CharField(
        verbose_name=_('Map title'),
        max_length=255,
        blank=True,
    )
    width = models.CharField(
        verbose_name=_('Width'),
        max_length=6,
        default='100%',
        help_text=_('Width of the map, including the CSS length units (e.g. "100%", "400px" or "400rem").'),
    )
    height = models.CharField(
        verbose_name=_('Height'),
        max_length=6,
        default='400px',
        help_text=_('Height of the map, including the CSS length units (e.g. "400px" or "400rem").'),
    )
    style = models.TextField(
        verbose_name=_('Map styling'),
        blank=True,
        help_text=_('Provide a valid (escaped) JSON configuration. See '
                    'http://developers.google.com/maps/documentation/javascript/styling'),
    )
    lat = models.FloatField(
        verbose_name=_('Latitude (lat)'),
        null=True,
        blank=True,
        help_text=_('Default Geographical latitude in degrees (e.g. "46.947973").'),
    )
    lng = models.FloatField(
        verbose_name=_('Longitude (lng)'),
        null=True,
        blank=True,
        help_text=_('Default Geographical longitude in degrees (e.g. "7.447446").'),
    )
    zoom = models.PositiveSmallIntegerField(
        verbose_name=_('Zoom level'),
        choices=ZOOM_LEVEL_CHOICES,
        default=13,
    )

    # control settings
    map_type_control = models.CharField(
        verbose_name=_('Map type'),
        choices=MAP_TYPE_CHOICES,
        default=MAP_TYPE_CHOICES[0][0],
        max_length=255,
    )
    zoom_control = models.BooleanField(
        verbose_name=_('Enable zooming'),
        default=True,
        help_text=_('Enabling zooming allows the user to view the map at different scales.'),
    )
    street_view_control = models.BooleanField(
        verbose_name=_('Enable Street View'),
        default=True,
        help_text=_('Street View allows the user to see street-level imagery.'),
    )
    rotate_control = models.BooleanField(
        verbose_name=_('Enable rotation'),
        default=True,
        help_text=_('Allows the user to change the orientation of the map.'),
    )
    scale_control = models.BooleanField(
        verbose_name=_('Enable map scale'),
        default=True,
        help_text=_('Displays a linear distance scale on the map.'),
    )
    fullscreen_control = models.BooleanField(
        verbose_name=_('Enable fullscreen mode'),
        default=True,
        help_text=_('Allows the user to select a fullscreen view of the map.'),
    )
    pan_control = models.BooleanField(
        verbose_name=_('Enable cursor key panning'),
        default=True,
        help_text=_('Allows the user to move the map using the cursor keys to see new areas.'),
    )
    double_click_zoom = models.BooleanField(
        verbose_name=_('Enable double-click zoom'),
        default=True,
        help_text=_('Allows the user to zoom and centre the map with a double-click or double-tap.'),
    )
    draggable = models.BooleanField(
        verbose_name=_('Enable dragging'),
        default=True,
        help_text=_('Allows the user to drag the map to see new areas.'),
    )
    keyboard_shortcuts = models.BooleanField(
        verbose_name=_('Enable keyboard shortcuts'),
        default=True,
        help_text=_('Allows the user to control the map using the keyboard.'),
    )
    scrollwheel = models.BooleanField(
        verbose_name=_('Enable scroll-wheel zooming'),
        default=True,
        help_text=_('Allows the user to control the zoom level with a scroll-wheel.'),
    )

    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        if self.title:
            return self.title
        return str(self.pk)

    def get_short_description(self):
        display = ''
        if self.title:
            display = '{0}, '.format(self.title)
        elif self.lat and self.lng:
            display += '{0} / {1}, '.format(self.lat, self.lng)
        display += '{0} x {1}'.format(self.width, self.height)
        return display

    def clean(self):
        if self.width and not CSS_WIDTH_RE.match(self.width):
            raise ValidationError(
                _('Width must be a positive integer followed by "px" or "%".')
            )
        if self.height and not CSS_HEIGHT_RE.match(self.height):
            raise ValidationError(
                _('Height must be a positive integer followed by "px".')
            )
        if self.style:
            try:
                json.loads(self.style)
            except ValueError:
                raise ValidationError(_('Map styling has to be valid JSON.'))


@python_2_unicode_compatible
class GoogleMapMarker(CMSPlugin):
    """
    Renders a marker inside the Google Maps wrapper
    """
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        blank=True,
    )
    address = models.CharField(
        verbose_name=_('Full address'),
        max_length=255,
        blank=True,
        help_text=_('Note: Latitude and longitude can be used to fine-tune the location.'),
    )
    lat = models.DecimalField(
        verbose_name=_('Latitude (lat)'),
        max_digits=10,
        decimal_places=6,
        null=True,
        blank=True,
        help_text=_('Geographical latitude in degrees (e.g. "46.947973").'),
    )
    lng = models.DecimalField(
        verbose_name=_('Longitude (lng)'),
        max_digits=10,
        decimal_places=6,
        null=True,
        blank=True,
        help_text=_('Geographical longitude in degrees (e.g. "7.447446").'),
    )
    icon = FilerImageField(
        verbose_name=_('Icon'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('A marker icon identifies a location on a map. '
                    'By default, it uses a standard image from Google.'),
    )
    # info window settings
    show_content = models.BooleanField(
        verbose_name=_('Show window'),
        default=True,
        help_text=_('Display the info window when the map loads.'),
    )
    info_content = models.TextField(
        verbose_name=_('Info window content'),
        blank=True,
        help_text=_('Will be displayed in the info window attached to the marker.'),
    )

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        display = []
        if self.title:
            display.append(self.title)
        if self.address:
            display.append(self.address)
        if self.lat and self.lng:
            display.append('{0} / {1} '.format(self.lat, self.lng))
        return ', '.join(display)


@python_2_unicode_compatible
class GoogleMapRoute(CMSPlugin):
    """
    Renders a route option inside the map
    """
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        blank=True,
    )
    origin = models.CharField(
        verbose_name=_('Starting address'),
        blank=True,
        max_length=255,
        help_text=_('Will be determined by user\'s location (if possible) if left blank.'),
    )
    destination = models.CharField(
        verbose_name=_('Destination address'),
        max_length=255,
    )
    travel_mode = models.CharField(
        verbose_name=_('Travel mode'),
        max_length=255,
        choices=TRAVEL_MODE_CHOICES,
        default=TRAVEL_MODE_CHOICES[0][0],
    )

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        display = ''
        if self.title:
            display = '{0}, '.format(self.title)
        if self.origin:
            display += 'from {0}, '.format(self.origin)
        display += 'to {0} '.format(self.destination)
        return display
