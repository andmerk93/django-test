import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DJANGO_DEBUG')

ALLOWED_HOSTS = ['*']

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
    'sorl.thumbnail',
    'sorl_thumbnail_serializer',
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

ROOT_URLCONF = 'core.urls'

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

AUTH_PASSWORD_VALIDATORS = [
    dict(NAME=f'django.contrib.auth.password_validation.{i}')
    for i in [
        'UserAttributeSimilarityValidator',
        'MinimumLengthValidator',
        'CommonPasswordValidator',
        'NumericPasswordValidator',
    ]
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Krasnoyarsk'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = dict(
    DEFAULT_PERMISSION_CLASSES=[
        'core.permissions.OwnerOrAdminOrReadOnly',
    ],

    DEFAULT_AUTHENTICATION_CLASSES=[
        'rest_framework.authentication.TokenAuthentication',
    ],
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

REDIS_HOST = os.getenv("REDIS_HOST", default="redis")
REDIS_PORT = os.getenv("REDIS_PORT", default="6379")

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_BROKER_TRANSPORT_OPTIONS = {"visibility_time_out": 3600}
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_USER_ID = 1

EMAIL_HOST = os.getenv("EMAIL_HOST", default="localhost")
EMAIL_PORT = os.getenv("EMAIL_PORT", default="25")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", default="user")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", default="pass")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", default="from@example.com") # noqa
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", default="django.core.mail.backends.dummy.EmailBackend") # noqa
