=========
Changelog
=========


1.4.0 (2020-01-29)
==================

* Added support for Django 3.0
* Add rendering on plugin first insert capability


1.3.1 (unreleased)
==================

* Added further tests to raise coverage
* Fixed smaller issues found during testing
* Changed ``DecimalField`` field to ``FloatField`` for **Marker** plugin


1.3.0 (2019-05-23)
==================

* Added support for Django 2.2 and django CMS 3.7
* Removed support for Django 2.0
* Extended test matrix
* Exclude tests folder from release build
* Added installation instructions for django-filer


1.2.0 (2018-11-07)
==================

* Fixed an issue with map not always setting correct zoom level
* Removed admin url data attribute from the map marker if cms isn't in edit mode
* Added support for Django 1.11, 2.0 and 2.1
* Removed support for Django 1.8, 1.9, 1.10
* Adapted testing infrastructure (tox/travis) to incorporate
  django CMS 3.5 and 4.0


1.1.1 (2017-06-16)
==================

* Refactored migration 0005 to avoid using the django CMS api because it can lead
  to database errors when the models on file don't match the ones in the migration.
* Moved Google Apps API Key to an environment variable on Divio Cloud


1.1.0 (2017-05-09)
==================

* Added support for customize marker icon
* Updated translations


1.0.2 (2017-01-10)
==================

* Fixed an issue where 0005 migration mismatches lat/lng values when creating
  the new nested structure from older upgrades
* Updated translations


1.0.1 (2016-11-22)
==================

* Prevent changes to ``DJANGOCMS_GOOGLEMAP_XXX`` settings from requiring new
  migrations
* Changed naming of ``Aldryn`` to ``Divio Cloud``
* Adapted testing infrastructure (tox/travis) to incorporate
  django CMS 3.4 and dropped 3.2
* Fixed zoom level not correctly being applied
* Fixed latitude/longitude data attribute values being incorrectly parsed for
  locales not using a period as decimal separator (e.g. german)


1.0.0 (2016-11-14)
==================

* Backwards incompatible changes
    * Deprecated template ``templates/cms/plugins/googlemap.html``
    * Moved template from ``templates/djangocms_googlemap/googlemap.html`` to
      ``templates/djangocms_googlemap/default/map.html``
    * Added setting ``DJANGOCMS_GOOGLEMAP_API_KEY``
    * Added setting ``DJANGOCMS_GOOGMEMAP_TEMPLATES``
    * Removed Django < 1.8 support
    * Removed ``alt`` attribute and migrated data to Filer
    * Migrated data to separated nested plugins ``Marker`` and ``Route``
* Cleaned up file structure
* Updated ``README.txt``
* Updated translations


0.5.2 (2016-09-08)
==================

* Added missing Django migration
* Added native Aldryn support


0.5.1 (2016-06-23)
==================

* Added missing South migration


0.5.0 (2016-06-22)
==================

* Added changelog
* Added fields to customise the map style
* Fixed an issue with multiple googlemaps plugins
* Moved JavaScript declarations into separate file
  ``static/djangocms_googlemap/djangocms.googlemaps.js``
* Used correct ``tempaltes/djangocms_googlemap`` folder,
  ``cms/plugins/googlemap.html`` will be removed in 1.0
