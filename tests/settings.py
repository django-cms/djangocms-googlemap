#!/usr/bin/env python
import os
import sys
import tempfile


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TESTS_DIR)

SECRET_KEY = 'djangocms-googlemap-test-key'
DEBUG = False
ALLOWED_HOSTS = ['localhost', 'testserver']
SITE_ID = 1
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'easy_thumbnails',
    'filer',
    'djangocms_googlemap',
    'tests',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(TESTS_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

ROOT_URLCONF = 'tests.urls'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(tempfile.gettempdir(), 'djangocms_googlemap_static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(tempfile.gettempdir(), 'djangocms_googlemap_media')

LANGUAGE_CODE = 'en'
LANGUAGES = [('en', 'English')]
CMS_LANGUAGES = {
    1: [{
        'code': 'en',
        'name': 'English',
    }]
}
CMS_TEMPLATES = [('page.html', 'Normal page')]
CMS_CONFIRM_VERSION4 = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


def run():
    sys.path.insert(0, ROOT_DIR)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

    import django
    from django.conf import settings
    from django.test.utils import get_runner

    django.setup()
    test_runner = get_runner(settings)(verbosity=1)
    failures = test_runner.run_tests(sys.argv[1:] or ['tests'])
    sys.exit(bool(failures))


if __name__ == '__main__':
    run()
