=========
Changelog
=========


1.0.1 (unreleased)
==================
* Prevent changes to ``DJANGOCMS_GOOGLEMAP_XXX`` settings from requiring new
  migrations
* Changed naming of ``Aldryn`` to ``Divio Cloud``
* Adapted testing infrastructure (tox/travis) to incorporate
  django CMS 3.4 and dropped 3.2


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
