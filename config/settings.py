"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

import pymysql

from .env_controller import Env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENV = Env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV.ENV("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV.ENV.bool("IS_DEBUG")


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "storages",
    "django_filters",
    "corsheaders",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.kakao",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "rest_framework_simplejwt.token_blacklist",
]

if DEBUG:
    THIRD_PARTY_APPS += [
        "django_extensions",
        "debug_toolbar",
    ]


USER_APPS = [
    "taxonomy",
    "photos",
    "quizzes",
    "core",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + USER_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ALLOWED_HOSTS = [ENV.ENV("PRODUCT_HOST_IP")]

if DEBUG:
    ALLOWED_HOSTS = ["10.0.2.2", "127.0.0.1", "localhost"]
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    INTERNAL_IPS = [
        "127.0.0.1",
        "localhost",
    ]
STATIC_ROOT = Path.joinpath(BASE_DIR, "static")


ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DB로 SQLite를 사용하는 경우

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# DB로 MySQL을 사용하는 경우

pymysql.install_as_MySQLdb()

DATABASES = {
    "default": {
        "ENGINE": ENV.ENV("DB_ENGINE"),
        "NAME": ENV.ENV("DB_NAME"),
        "USER": ENV.ENV("DB_USER"),
        "PASSWORD": ENV.ENV("DB_PASSWORD"),
        "HOST": ENV.ENV("DB_HOST"),
        "PORT": ENV.ENV("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    # ],
    "DEFAULT_PERMISSION_CLASSES": (
        # "rest_framework.permissions.IsAuthenticatedOrReadOnly",
        "rest_framework.permissions.AllowAny",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework.authentication.SessionAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 30,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

if DEBUG:
    REST_FRAMEWORK.update(
        {
            "DEFAULT_RENDERER_CLASSES": [
                "rest_framework.renderers.JSONRenderer",
                "rest_framework.renderers.BrowsableAPIRenderer",
            ]
        }
    )


AUTH_USER_MODEL = "core.User"

DEFAULT_FILE_STORAGE = "core.storages.S3DefaultStorage"
# STATICFILES_STORAGE = "core.storages.S3StaticStorage"

AWS_ACCESS_KEY_ID = ENV.ENV("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = ENV.ENV("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_ACL = ENV.ENV("AWS_DEFAULT_ACL")
AWS_S3_REGION_NAME = ENV.ENV("AWS_S3_REGION_NAME")
AWS_S3_SIGNATURE_VERSION = ENV.ENV("AWS_S3_SIGNATURE_VERSION")
AWS_STORAGE_BUCKET_NAME = ENV.ENV("AWS_STORAGE_BUCKET_NAME")
AWS_CLOUDFRONT_DOMAIN = ENV.ENV("AWS_CLOUDFRONT_DOMAIN")

MEDIA_URL = f"https://{AWS_CLOUDFRONT_DOMAIN}/"

CORS_ALLOWED_ORIGIN = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    ENV.ENV("PRODUCT_HOST_IP"),
]
CORS_ALLOW_CREDENTIALS = True


ACCOUNT_USER_MODEL_USERNAME_FIELD = None  # username 필드 사용 x
ACCOUNT_EMAIL_REQUIRED = True  # email 필드 사용 o
ACCOUNT_USERNAME_REQUIRED = False  # username 필드 사용 x
ACCOUNT_AUTHENTICATION_METHOD = "email"

SITE_ID = 1
REST_USE_JWT = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "core.serializers.UserCustomSerializer",
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
}
