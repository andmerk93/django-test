"""
Django settings for django_test project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'treasuremap',
    'django_summernote',
    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_test.urls'

TEMPLATES = [
    dict(
        BACKEND='django.template.backends.django.DjangoTemplates',
        DIRS=[BASE_DIR / 'templates'],
        APP_DIRS=True,
        OPTIONS=dict(
            context_processors=[
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        ),
    ),
]

WSGI_APPLICATION = 'django_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


if DEBUG:
    DATABASES = dict(
        default=dict(
            ENGINE='django.db.backends.sqlite3',
            NAME=(BASE_DIR / 'db.sqlite3'),
        )
    )
else:
    DATABASES = dict(
        default=dict(
            ENGINE=os.getenv('DB_ENGINE'),
            NAME=os.getenv('DB_NAME'),
            USER=os.getenv('DB_USER'),
            PASSWORD=os.getenv('DB_PASSWORD'),
            HOST=os.getenv('DB_HOST'),
            PORT=os.getenv('DB_PORT'),
        )
    )

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    dict(NAME=f'django.contrib.auth.password_validation.{i}')
    for i in [
        'UserAttributeSimilarityValidator',
        'MinimumLengthValidator',
        'CommonPasswordValidator',
        'NumericPasswordValidator',
    ]
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Krasnoyarsk'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = dict(
#    DEFAULT_PERMISSION_CLASSES=[
#        'rest_framework.permissions.IsAuthenticated',
#    ],

#    DEFAULT_AUTHENTICATION_CLASSES=[
#        'rest_framework.authentication.TokenAuthentication',
#    ],
    DEFAULT_PAGINATION_CLASS='rest_framework.pagination.PageNumberPagination',
    PAGE_SIZE=10,
    DEFAULT_RENDERER_CLASSES=(
        'rest_framework.renderers.JSONRenderer',
    ),
    DATETIME_FORMAT='%Y-%m-%d, %H:%M:%S',
)

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += ('rest_framework.renderers.BrowsableAPIRenderer',)  # noqa

TREASURE_MAP = dict(
    BACKEND='treasuremap.backends.yandex.YandexMapBackend',
    ONLY_MAP=False,
    SIZE=(500, 400),
    MAP_OPTIONS=dict(
        latitude=56.008838,
        longitude=92.840162,
        zoom=5
    )
)

SUMMERNOTE_CONFIG = dict(
    lang='ru-RU'
)

OWM_API_KEY = os.getenv('OWM_API_KEY')