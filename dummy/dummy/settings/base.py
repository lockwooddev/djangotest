# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DJANGO_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fk!_u^5*yhmgv1vgo9v!6)wc7+)v82)%q@0@kc92vd&tu(kp$%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Django Apps
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'dummy.apps.users',

    'south',
    'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.SHA1PasswordHasher',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'dummy.urls'

WSGI_APPLICATION = 'dummy.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'web', 'static'))
MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'web', 'media'))

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# Custom User Model
AUTH_USER_MODEL = 'users.User'

LOGIN_URL = '/login/'