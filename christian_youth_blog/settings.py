"""
Django settings for christian_youth_blog project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url
if os.path.isfile("env.py"):
    import env


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'cy-django-blog-486df1fc929f.herokuapp.com',
    '8000-lanreandero-cipp4django-b42ah2no9xi.ws-eu108.gitpod.io',
    'localhost',
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

ADMIN_URL = 'admin/'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'corsheaders',
    'cloudinary',
    'crispy_forms',
    'crispy_bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_summernote',
    'blog',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

cloudinary.config(
    cloud_name='dmwocs4qe',
    api_key='134374111236266',
    api_secret='Jq2ddAoUbCj59Epng85km0hojOA',
    secure=True,
)

DJANGO_SUMMERNOTE_CONFIG = {
    'iframe': False,
    'summernote': {
        'width': '100%',
        'height': '480',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview']],
        ],
    },
}

CSRF_COOKIE_SECURE = True

CSRF_COOKIE_SAMESITE = 'None'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'christian_youth_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'christian_youth_blog.wsgi.application'


DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}


CSRF_TRUSTED_ORIGINS = [
    "https://8000-lanreandero-cipp4django-b42ah2no9xi.ws-eu108.gitpod.io",
    "https://cy-django-blog-486df1fc929f.herokuapp.com"
    "https://*.herokuapp.com",
    "https://*.gitpod.io",
]


CORS_ALLOWED_ORIGINS = [
    "https://8000-lanreandero-cipp4django-b42ah2no9xi.ws-eu108.gitpod.io",
    "https://cy-django-blog-486df1fc929f.herokuapp.com"
    "https://*.herokuapp.com",
    "https://*.gitpod.io",
    "https://ui.dev",
]


SHOULD_APPROVE_USER_POSTS = True


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STATIC_URL = '/static/'
STATICFILES_STORAGE = (
    'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
