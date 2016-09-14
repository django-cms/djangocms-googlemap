from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible

from filer.fields.image import FilerFileField

from parler.models import TranslatableModel, TranslatedFields


@python_2_unicode_compatible
class GoogleMap(CMSPlugin):
    """
    A google maps integration
    """
    translatable_content_excluded_fields = ['width', 'height']

    style = models.TextField(_("custom map style"), blank=True,
        help_text=_('Provide a valid JSON configuration (escaped). See '
            'developers.google.com/maps/documentation/javascript/styling'))

    ZOOM_LEVELS = map(lambda c: (c, str(c)), range(22))
    zoom = models.PositiveSmallIntegerField(
        _("zoom level"), choices=ZOOM_LEVELS, default=13)

    route_planer_title = models.CharField(
        _("route planner title"), max_length=150, blank=True, null=True,
        default=_('Calculate your fastest way to here'))

    route_planer = models.BooleanField(_("route planner"), default=False)

    width = models.CharField(
        _('width'), max_length=6, default='100%',
        help_text=_('Plugin width (in pixels or percent).'))

    height = models.CharField(
        _('height'), max_length=6, default='400px',
        help_text=_('Plugin height (in pixels).'))

    scrollwheel = models.BooleanField(
        _('scrollwheel'), default=True,
        help_text=_('Enable scrollwheel zooming on the map'))

    double_click_zoom = models.BooleanField(
        _('double click zoom'), default=True)

    draggable = models.BooleanField(_('draggable'), default=True)

    keyboard_shortcuts = models.BooleanField(
        _('keyboard shortcuts'), default=True)

    pan_control = models.BooleanField(_('Pan control'), default=True)

    zoom_control = models.BooleanField(_('zoom control'), default=True)

    street_view_control = models.BooleanField(
        _('Street View control'), default=True)

    def __str__(self):
        return ""


@python_2_unicode_compatible
class GoogleMapLocation(CMSPlugin):
    translatable_content_excluded_fields = ['address', 'zipcode', ]

    title = models.CharField(_("map title"), max_length=100, blank=True, null=True)

    address = models.CharField(_("address"), max_length=150)
    zipcode = models.CharField(_("zip code"), max_length=30)
    city = models.CharField(_("city"), max_length=100)

    content = models.CharField(
        _("additional content"), max_length=255, blank=True,
        help_text=_('Displayed under address in the bubble.'))

    lat = models.DecimalField(
        _('latitude'), max_digits=10, decimal_places=6, null=True, blank=True,
        help_text=_('Use latitude & longitude to fine tune the map position.'))

    lng = models.DecimalField(
        _('longitude'), max_digits=10, decimal_places=6, null=True, blank=True)

    info_window = models.BooleanField(
        _('info window'), default=True,
        help_text=_('Show textbox over marker'))

    marker_icon = FilerFileField(
        null=True,
        blank=True,
        help_text=_('Map marker icon. Leave empty for the default red Google Map pin.')
    )

    def get_title(self):
        if self.title is None:
            return _("Map")
        return self.title

    def get_lat_lng(self):
        if self.lat and self.lng:
            return self.lat, self.lng

    def __str__(self):
        return u"%s (%s, %s %s)" % (self.get_title(), self.address,
                                    self.zipcode, self.city, )
