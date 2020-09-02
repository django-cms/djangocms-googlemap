from django.conf import settings
from django.core.exceptions import ValidationError
from django.test import TestCase

from djangocms_googlemap.models import (
    MAP_TYPE_CHOICES, TRAVEL_MODE_CHOICES, ZOOM_LEVEL_CHOICES, GoogleMap,
    GoogleMapMarker, GoogleMapRoute, get_templates,
)

from .helpers import get_filer_image


SAMPLE_STYLES = """
[{"elementType": "geometry", "stylers": [{"color": "#242f3e"}]},
{"elementType": "labels.text.stroke", "stylers": [{"color": "#242f3e"}]},
{"elementType": "labels.text.fill", "stylers": [{"color": "#746855"}]}]
"""


class GoogleMapModelTestCase(TestCase):

    def setUp(self):
        self.icon = get_filer_image("pin.png")

    def tearDown(self):
        if self.icon:
            self.icon.delete()

    def test_settings(self):
        self.assertEqual(get_templates(), [("default", "Default")])
        settings.DJANGOCMS_GOOGLEMAP_TEMPLATES = [("feature", "Feature")]
        self.assertEqual(get_templates(), [("default", "Default"), ("feature", "Feature")])

    def test_googlemap_instance(self):
        GoogleMap.objects.create(
            template="default",
            title="some title",
            width="400px",
            height="200px",
            style=SAMPLE_STYLES,
            lat=40.730610,
            lng=-73.935242,
            zoom=int(ZOOM_LEVEL_CHOICES[11][1]),
            map_type_control=MAP_TYPE_CHOICES[0][1],
            zoom_control=False,
            street_view_control=False,
            rotate_control=False,
            scale_control=False,
            fullscreen_control=False,
            pan_control=False,
            double_click_zoom=False,
            draggable=False,
            keyboard_shortcuts=False,
            scrollwheel=False,
        )
        instance = GoogleMap.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = GoogleMap.objects.first()
        self.assertEqual(instance.template, "default")
        self.assertEqual(instance.title, "some title")
        self.assertEqual(instance.width, "400px")
        self.assertEqual(instance.height, "200px")
        self.assertEqual(instance.style, SAMPLE_STYLES)
        self.assertEqual(instance.lat, 40.73061)
        self.assertEqual(instance.lng, -73.935242)
        self.assertEqual(instance.zoom, 11)
        self.assertEqual(instance.map_type_control, "ROADMAP")
        self.assertFalse(instance.zoom_control)
        self.assertFalse(instance.street_view_control)
        self.assertFalse(instance.rotate_control)
        self.assertFalse(instance.scale_control)
        self.assertFalse(instance.fullscreen_control)
        self.assertFalse(instance.pan_control)
        self.assertFalse(instance.double_click_zoom)
        self.assertFalse(instance.draggable)
        self.assertFalse(instance.keyboard_shortcuts)
        self.assertFalse(instance.scrollwheel)
        # test methods
        self.assertEqual(str(instance), "some title")
        self.assertEqual(
            instance.get_short_description(),
            "some title, 400px x 200px",
        )
        instance.title = None
        self.assertEqual(str(instance), "1")
        self.assertEqual(
            instance.get_short_description(),
            "40.73061 / -73.935242, 400px x 200px",
        )
        instance.lat = None
        instance.lng = None
        self.assertEqual(
            instance.get_short_description(),
            "400px x 200px",
        )
        # assert validation errors
        self.assertIsNone(instance.clean())
        with self.assertRaises(ValidationError):
            instance.width = "200test"
            instance.clean()
        instance.width = "200px"
        with self.assertRaises(ValidationError):
            instance.height = "200tpd"
            instance.clean()
        instance.height = "200px"
        with self.assertRaises(ValidationError):
            instance.style = SAMPLE_STYLES + "[{'elementType': 'geometry',]"
            instance.clean()

    def test_googlemap_marker_instance(self):
        GoogleMapMarker.objects.create(
            title="some title",
            address="Main road, New York",
            lat=40.730610,
            lng=-73.935242,
            icon=self.icon,
            show_content=False,
            info_content="Some content to display",
        )
        instance = GoogleMapMarker.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = GoogleMapMarker.objects.first()
        self.assertEqual(instance.title, "some title")
        self.assertEqual(instance.address, "Main road, New York")
        self.assertEqual(instance.lat, 40.73061)
        self.assertEqual(instance.lng, -73.935242)
        self.assertEqual(instance.icon, self.icon)
        self.assertFalse(instance.show_content)
        self.assertEqual(instance.info_content, "Some content to display")
        # test methods
        self.assertEqual(str(instance), "1")
        self.assertEqual(
            instance.get_short_description(),
            "some title, Main road, New York, 40.73061 / -73.935242",
        )
        instance.title = None
        self.assertEqual(
            instance.get_short_description(),
            "Main road, New York, 40.73061 / -73.935242",
        )
        instance.address = None
        self.assertEqual(
            instance.get_short_description(),
            "40.73061 / -73.935242",
        )
        instance.lat = None
        self.assertEqual(instance.get_short_description(), "")

    def test_googlemap_route_instance(self):
        GoogleMapRoute.objects.create(
            title="some title",
            origin="starting address",
            destination="destination address",
            travel_mode=TRAVEL_MODE_CHOICES[1][0],
        )
        instance = GoogleMapRoute.objects.all()
        self.assertEqual(instance.count(), 1)
        instance = GoogleMapRoute.objects.first()
        self.assertEqual(instance.title, "some title")
        self.assertEqual(instance.origin, "starting address")
        self.assertEqual(instance.destination, "destination address")
        self.assertEqual(instance.travel_mode, "BICYCLING")
        # test methods
        self.assertEqual(str(instance), "1")
        self.assertEqual(
            instance.get_short_description(),
            "some title, from starting address, to destination address",
        )
        instance.title = None
        self.assertEqual(
            instance.get_short_description(),
            "from starting address, to destination address",
        )
        instance.origin = None
        self.assertEqual(
            instance.get_short_description(),
            "to destination address",
        )
