from cms.api import add_plugin, create_page
from cms.test_utils.testcases import CMSTestCase

from djangocms_googlemap.cms_plugins import (
    GoogleMapMarkerPlugin, GoogleMapPlugin, GoogleMapRoutePlugin,
)

from .helpers import get_filer_image


class GoogleMapPluginsTestCase(CMSTestCase):

    def setUp(self):
        self.language = "en"
        self.home = create_page(
            title="home",
            template="page.html",
            language=self.language,
        )
        self.home.publish(self.language)
        self.page = create_page(
            title="content",
            template="page.html",
            language=self.language,
        )
        self.page.publish(self.language)
        self.placeholder = self.page.placeholders.get(slot="content")
        self.superuser = self.get_superuser()
        self.icon = get_filer_image("pin.png")

    def tearDown(self):
        self.page.delete()
        self.home.delete()
        self.superuser.delete()
        if self.icon:
            self.icon.delete()

    def test_googlemap_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=GoogleMapPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()  # should not raise an error
        self.assertEqual(plugin.plugin_type, "GoogleMapPlugin")

    def test_googlemap_marker_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=GoogleMapMarkerPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()  # should not raise an error
        self.assertEqual(plugin.plugin_type, "GoogleMapMarkerPlugin")

    def test_googlemap_route_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=GoogleMapRoutePlugin.__name__,
            language=self.language,
            destination="some destination",
        )
        plugin.full_clean()  # should not raise an error
        self.assertEqual(plugin.plugin_type, "GoogleMapRoutePlugin")

    def test_plugin_structure(self):
        request_url = self.page.get_absolute_url(self.language) + "?toolbar_off=true"

        parent = add_plugin(
            placeholder=self.placeholder,
            plugin_type=GoogleMapPlugin.__name__,
            language=self.language,
        )
        self.page.publish(self.language)
        self.assertEqual(parent.get_plugin_class_instance().name, "Google Map")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertContains(response, 'div class="djangocms-googlemap')
        self.assertContains(response, 'script src="https://maps.googleapis.com/maps/api/js')
        self.assertContains(response, 'script src="/static/djangocms_googlemap/js/djangocms.googlemap.js')

        child = add_plugin(
            target=parent,
            placeholder=self.placeholder,
            plugin_type=GoogleMapMarkerPlugin.__name__,
            language=self.language,
        )
        self.page.publish(self.language)
        self.assertEqual(child.get_plugin_class_instance().name, "Marker")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertContains(response, 'div class="djangocms-googlemap-marker')

        child = add_plugin(
            target=parent,
            placeholder=self.placeholder,
            plugin_type=GoogleMapRoutePlugin.__name__,
            language=self.language,
        )
        self.page.publish(self.language)
        self.assertEqual(child.get_plugin_class_instance().name, "Route")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertContains(response, 'div class="djangocms-googlemap-route')
