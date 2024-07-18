from .base import *

DEBUG = False

ALLOWED_HOSTS = [
        "*",
        ]

CSRF_TRUSTED_ORIGINS = ['https://vitainfo.kr']

CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': config.USER,
        'PASSWORD': config.PASSWORD,
        'HOST': 'database-1.c1eucoags0zw.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"

# Medial files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media/'
