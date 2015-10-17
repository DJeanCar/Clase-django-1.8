from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'proyecto',
        'USER': 'proyecto',
        'PASSWORD': 'proyecto',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'