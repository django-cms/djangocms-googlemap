djangocms-googlemap
===================

A Google Maps plugin for django CMS.


Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`_, run ``pip install djangocms-googlemap``.
* Add ``'djangocms_googlemap'`` to your ``INSTALLED_APPS`` setting.
* If using Django 1.6 and South < 1.0.2 add ``'djangocms_googlemap': 'djangocms_googlemap.migrations_django',``
  to ``SOUTH_MIGRATION_MODULES`` (or define ``SOUTH_MIGRATION_MODULES`` if it
  does not exists);
* Run ``manage.py migrate djangocms_googlemap``.


Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-googlemap/

