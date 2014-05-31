from .base import *

import os


DJANGO_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

SECRET_KEY = 'testsecret01234567890'

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
    }
}

TEMPLATE_DIRS = (
    os.path.join(DJANGO_DIR, 'templates'),
)
