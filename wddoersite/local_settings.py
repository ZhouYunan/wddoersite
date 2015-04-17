# coding: utf-8

# DEBUG = False
# TEMPLATE_DEBUG = DEBUG
# ALLOWED_HOSTS = ['*']



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wddoersitedb',
        'USER': 'postgres',
        'PASSWORD': '1239',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

import os

BASE_DIR = 'D:/work/wddoersite'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATICFILES_DIRS = (
    ("css", os.path.join(BASE_DIR, 'static/css')),
    ("fonts", os.path.join(BASE_DIR, 'static/fonts')),
    ("js", os.path.join(BASE_DIR, 'static/js')),
)
