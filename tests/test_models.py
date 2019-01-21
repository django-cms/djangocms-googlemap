# -*- coding: utf-8 -*-
from django.test import TestCase

from djangocms_googlemap.models import GoogleMap


class GoogleMapTestCase(TestCase):

    def setUp(self):
        GoogleMap.objects.create(
            title='test',
        )

    def test_google_map_instance(self):
        """Google Map instance has been created"""
        google_map = GoogleMap.objects.get(title='test')
        self.assertEqual(google_map.title, 'test')
