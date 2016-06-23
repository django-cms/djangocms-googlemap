#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

from djangocms_googlemap import __version__

REQUIREMENTS = [
    'Django>=1.8',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='djangocms-googlemap',
    version=__version__,
    description='Google Maps plugin for django CMS',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/divio/djangocms-googlemap',
    packages=[
        'djangocms_googlemap',
        'djangocms_googlemap.migrations',
        'djangocms_googlemap.south_migrations'
    ],
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False
)
