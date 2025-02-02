"""
Django settings for eco project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-f84^xyx#!5ci98mijkurowrv)03ta)gisxjhr6p#bacfu36i@^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.221.15', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'whitenoise.runserver_nostatic',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'djoser',
    'bootstrap5',
    "core",
    "store",
    "front"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "eco.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
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

# UNFOLD = {
#     "SITE_TITLE": None,
#     "SITE_HEADER": None,
#     "SITE_URL": "/",
#     # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
#     "SITE_ICON": {
#         "light": lambda request: static("icon-light.svg"),  # light mode
#         "dark": lambda request: static("icon-dark.svg"),  # dark mode
#     },
#     # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
#     "SITE_LOGO": {
#         "light": lambda request: static("logo-light.svg"),  # light mode
#         "dark": lambda request: static("logo-dark.svg"),  # dark mode
#     },
#     "SITE_SYMBOL": "speed",  # symbol from icon set
#     "SITE_FAVICONS": [
#         {
#             "rel": "icon",
#             "sizes": "32x32",
#             "type": "image/svg+xml",
#             "href": lambda request: static("favicon.svg"),
#         },
#     ],
#     "SHOW_HISTORY": True, # show/hide "History" button, default: True
#     "SHOW_VIEW_ON_SITE": True, # show/hide "View on site" button, default: True
#     "ENVIRONMENT": "sample_app.environment_callback",
#     "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",
#     "THEME": "dark", # Force theme: "dark" or "light". Will disable theme switcher
#     "LOGIN": {
#         "image": lambda request: static("sample/login-bg.jpg"),
#         "redirect_after": lambda request: reverse_lazy("admin:APP_MODEL_changelist"),
#     },
#     "STYLES": [
#         lambda request: static("css/style.css"),
#     ],
#     "SCRIPTS": [
#         lambda request: static("js/script.js"),
#     ],
#     "COLORS": {
#         "primary": {
#             "50": "250 245 255",
#             "100": "243 232 255",
#             "200": "233 213 255",
#             "300": "216 180 254",
#             "400": "192 132 252",
#             "500": "168 85 247",
#             "600": "147 51 234",
#             "700": "126 34 206",
#             "800": "107 33 168",
#             "900": "88 28 135",
#             "950": "59 7 100",
#         },
#     },
#     "EXTENSIONS": {
#         "modeltranslation": {
#             "flags": {
#                 "en": "🇬🇧",
#                 "fr": "🇫🇷",
#                 "nl": "🇧🇪",
#             },
#         },
#     },
#     "SIDEBAR": {
#         "show_search": False,  # Search in applications and models names
#         "show_all_applications": False,  # Dropdown with all applications and models
#         "navigation": [
#             {
#                 "title": _("Navigation"),
#                 "separator": True,  # Top border
#                 "collapsible": True,  # Collapsible group of links
#                 "items": [
#                     {
#                         "title": _("Dashboard"),
#                         "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
#                         "link": reverse_lazy("admin:index"),
#                         "badge": "sample_app.badge_callback",
#                         "permission": lambda request: request.user.is_superuser,
#                     },
#                     {
#                         "title": _("Users"),
#                         "icon": "people",
#                         "link": reverse_lazy("admin:users_user_changelist"),
#                     },
#                 ],
#             },
#         ],
#     },
#     "TABS": [
#         {
#             "models": [
#                 "app_label.model_name_in_lowercase",
#             ],
#             "items": [
#                 {
#                     "title": _("Your custom title"),
#                     "link": reverse_lazy("admin:app_label_model_name_changelist"),
#                     "permission": "sample_app.permission_callback",
#                 },
#             ],
#         },
#     ],
# }


# def dashboard_callback(request, context):
#     """
#     Callback to prepare custom variables for index template which is used as dashboard
#     template. It can be overridden in application by creating custom admin/index.html.
#     """
#     context.update(
#         {
#             "sample": "example",  # this will be injected into templates/admin/index.html
#         }
#     )
#     return context


# def environment_callback(request):
#     """
#     Callback has to return a list of two values represeting text value and the color
#     type of the label displayed in top right corner.
#     """
#     return ["Production", "danger"] # info, danger, warning, success


# def badge_callback(request):
#     return 3

# def permission_callback(request):
#     return request.user.has_perm("sample_app.change_model")

WSGI_APPLICATION = "eco.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#? Database in local system

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecodb',  # Your database name
        'USER': 'postgres',  # Your database user
        'PASSWORD': '1q2w3e4r5t6yAli!!',  # Your database password
        'HOST': 'localhost',  # Host where PostgreSQL is running
        'PORT': '5432',  # Leave empty for default port (5432)
    }
}

#? Database in Server


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'core.User'
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "fa-ir"

TIME_ZONE = "Asia/Tehran"

USE_THOUSAND_SEPARATOR = True

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
MEDIA_ROOT = BASE_DIR/'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
}


SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
   'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
}

AUTH_USER_MODEL = 'core.User'

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'core.serializers.UserCreateSerializer',
        'current_user': 'core.serializers.UserSerializer',
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
