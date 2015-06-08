# coding: utf-8

import os

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wddoersite.blog_pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'wddoersite.urls'

BASE_DIR = 'D:/webprojects/wddoersite'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'wddoersite/blog/templates')
        ],
        'OPTIONS': {
            'context_processors': [
                "django.core.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ]
        },
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',     # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'wddoersitedb',
        'USER': 'root',
        'PASSWORD': '1239',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'default-character-set': 'utf-8',
    }
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'wddoersite/blog/templates').replace('\\', '/'),
    os.path.join(BASE_DIR, 'wddoersite/iadmin/templates').replace('\\', '/'),
    os.path.join(BASE_DIR, 'wddoersite/stock/templates').replace('\\', '/'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'wddoersite/blog/static').replace('\\', '/'),
    os.path.join(BASE_DIR, 'wddoersite/iadmin/static').replace('\\', '/'),
    os.path.join(BASE_DIR, 'wddoersite/stock/static').replace('\\', '/'),
)

AUTH_USER_MODEL = "iadmin.User"
