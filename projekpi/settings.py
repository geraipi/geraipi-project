"""
Django settings for projekpi project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.forms",
    "corsheaders",
    "django_filters",
    "import_export",
    "loginas",
    "profiles",
    "master",
    "frontend",
    "store",
    "produk",
    "rest_framework",
    "tailwind",
    "theme",
    # "django_browser_reload",
    "rest_framework.authtoken",
    "ckeditor",
    "apidata",
    "django_extensions",
    "webpack_loader",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "django_htmx.middleware.HtmxMiddleware",
    # "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = ["http://localhost:8000"]
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     "http://localhost:4000"
# ]
ROOT_URLCONF = "projekpi.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

NPM_BIN_PATH = "/usr/bin/npm"

TAILWIND_APP_NAME = "theme"

WSGI_APPLICATION = "projekpi.wsgi.application"

USE_TZ = True
TIME_ZONE = "Asia/Jakarta"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME", "geraipi"),
        "USER": os.getenv("DB_USER", "root"),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": "3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

USE_TZ = True

# SESSION_COOKIE_SAMESITE = "None"  # As a string
# SESSION_COOKIE_SECURE = True
# X_FRAME_OPTIONS = "ALLOWALL"
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, "static")
if not DEBUG:
    STATIC_ROOT = os.getenv("STATIC_PATH", os.path.join(BASE_DIR, "static"))
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
STATIC_URL = "static/"

MEDIA_ROOT = os.getenv("MEDIA_PATH", os.path.join(BASE_DIR, "media"))
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
NPM_BIN_PATH = os.getenv("NPM_ENV")
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}

AUTH_USER_MODEL = "profiles.UserProfile"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", False)
EMAIL_HOST = os.getenv("EMAIL_HOST", "geraipi")
EMAIL_PORT = os.getenv("EMAIL_PORT", 465)
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "email@testnet.geraipi.id")
EMAIL_HOST_PASSWORD = ("EMAIL_HOST_PASSWORD", "geraipi")

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_FILENAME_GENERATOR = "utils.get_filename"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Bold", "Italic", "Underline"],
            [
                "NumberedList",
                "BulletedList",
                "-",
                "Outdent",
                "Indent",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            ["Link", "Unlink"],
            ["RemoveFormat", "Source"],
        ],
    }
}
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

LANGUAGE_CODE = "en"

USE_I18N = True

USE_L10N = True

USE_TZ = True

CELERY_TIMEZONE = "Asia/Jakarta"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60


# CELERY_IMPORTS = ("tasks",)
def CAN_LOGIN_AS(request, target_user):
    return request.user.is_superuser


LOGINAS_LOGOUT_REDIRECT_URL = reverse_lazy("admin:index")
LOGINAS_REDIRECT_URL = "/admin"
X_FRAME_OPTIONS = "ALLOW-FROM *"
SESSION_COOKIE_SAMESITE = "None"  # As a string
SESSION_COOKIE_SECURE = True
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'webpack_bundles/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    }
}
