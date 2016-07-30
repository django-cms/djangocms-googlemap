from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import GoogleMapForm
from .models import GoogleMap, GoogleMapLocation

from cms.utils.urlutils import static_with_version


class GoogleMapPlugin(CMSPluginBase):
    model = GoogleMap
    name = _("Google Map")
    render_template = "cms/plugins/googlemap.html"
    admin_preview = False
    form = GoogleMapForm
    fieldsets = (
        (None, {
            'fields': ('zoom', ('width', 'height',)),
        }),
        (_('Advanced'), {
            'fields': ('route_planer', 'route_planer_title', 'scrollwheel',
                       'double_click_zoom', 'draggable', 'keyboard_shortcuts',
                       'pan_control', 'zoom_control', 'street_view_control',
                       'style', ),
        }),
    )

    allow_children = True
    child_classes = ['GoogleMapLocationPlugin']

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(GoogleMapPlugin)


class GoogleMapLocationPlugin(CMSPluginBase):
    model = GoogleMapLocation
    name = _("Google Map Location")
    render_template = "djangocms_googlemap/googlemap-location.html"

    allow_children = False
    parent_classes = ['GoogleMapPlugin']

    # TODO: remove this as soon as the bug is fixed in DjangoCMS
    # https://github.com/divio/django-cms/issues/5476
    # This has to do with the cms.models.fields.PageField that doesn't include the bundle as it should (regression)
    class Media:
        js = (
            static_with_version('cms/js/dist/bundle.admin.base.min.js'),
        )


plugin_pool.register_plugin(GoogleMapLocationPlugin)
