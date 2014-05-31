from .base import *

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [u'']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lockwood',
        'USER': 'lockwood',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

TEMPLATE_DIRS = (
    os.path.join(DJANGO_DIR, 'templates'),
)

STATICFILES_DIRS = (
    os.path.normpath(os.path.join(DJANGO_DIR, 'static')),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {'format': '%(levelname)s %(asctime)s %(name)s %(message)s'},
        'request': {'format': '%(levelname)s %(asctime)s %(name)s %(message)s\n%(request)s'},
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.normpath(os.path.join('/tmp', 'django.log')),
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.request': {
           'handlers': ['console', 'file'],
           'level': 'ERROR',
           'propagate': False,
        },
        'django': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'south': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'dummy': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}
