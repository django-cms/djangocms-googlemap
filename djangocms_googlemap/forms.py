# coding: utf-8
from distutils.version import LooseVersion
import re
import django
import json

from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from .models import GoogleMap


DJANGO_1_5 = LooseVersion(django.get_version()) < LooseVersion('1.6')
CSS_WIDTH_RE = re.compile(r'^\d+(?:px|%)$')
CSS_HEIGHT_RE = re.compile(r'^\d+px$')


class GoogleMapForm(ModelForm):
    class Meta:
        model = GoogleMap
        if not DJANGO_1_5:
            fields = '__all__'

    def clean(self):
        cleaned_data = super(GoogleMapForm, self).clean()
        width = cleaned_data.get('width', '')
        height = cleaned_data.get('height', '')
        if width or height:
            if width and not CSS_WIDTH_RE.match(width):
                self._errors['width'] = self.error_class([
                    _(u'Must be a positive integer followed by “px” or “%”.')])
            if height and not CSS_HEIGHT_RE.match(height):
                self._errors['height'] = self.error_class([
                    _(u'Must be a positive integer followed by “px”.')])
        return cleaned_data

    def clean_style(self):
        style = self.cleaned_data.get('style', '').strip()
        if style:
            try:
                json.loads(style)
            except ValueError:
                raise ValidationError('Has to be valid JSON', code='invalid')
        return style
