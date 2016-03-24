from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import GoogleMapForm
from .models import GoogleMap


class GoogleMapPlugin(CMSPluginBase):
    model = GoogleMap
    name = _("Google Map")
    render_template = "cms/plugins/googlemap.html"
    admin_preview = False
    form = GoogleMapForm
    fieldsets = (
        (None, {
            'fields': ('title', 'address', ('zipcode', 'city',),
                       'content', 'zoom', ('lat', 'lng'),),
        }),
        (_('Advanced'), {
            'fields': (('route_planer', 'route_planer_title'),
                       ('width', 'height',), 'info_window', 'scrollwheel',
                       'double_click_zoom', 'draggable', 'keyboard_shortcuts',
                       'pan_control', 'zoom_control', 'street_view_control',
                       'style'),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(GoogleMapPlugin)
