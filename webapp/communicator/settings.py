#Django settings for communicator project.
import os

PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
            ('en', 'English'),
]

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, "static")
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_PATH + '/media/',
)

# List of finder classes that know how to find static files in various 
# locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

HAYSTACK_CONNECTIONS = {
    'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'communicator.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'communicator.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crisis',
    'refugeecenter',
    'person',
    'assessment',
    'resources',
    'bootstrap_toolkit',
    'haystack',
)

from local_settings import *
