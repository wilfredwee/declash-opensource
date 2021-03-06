"""
Django settings for DeClash project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'twp_pc&@h!sg)sw3nja&x)8%ihr^9u-oijzm!dhqr0a-u*alwt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '*'
    ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rocketscience',
    'autocomplete_light',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DeClash.urls'

WSGI_APPLICATION = 'DeClash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# if not DEBUG:
#     DATABASES = {
#         'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ['RDS_DB_NAME'],
#         'USER': os.environ['RDS_USERNAME'],
#         'PASSWORD': os.environ['RDS_PASSWORD'],
#         'HOST': os.environ['RDS_HOSTNAME'],
#         'PORT': os.environ['RDS_PORT'],
#         }
#     }
#     REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#     )
#     }

# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': os.environ['RDS_DB_NAME'],
#     'USER': os.environ['RDS_USERNAME'],
#     'PASSWORD': os.environ['RDS_PASSWORD'],
#     'HOST': os.environ['RDS_HOSTNAME'],
#     'PORT': os.environ['RDS_PORT'],
#     }
# }
# REST_FRAMEWORK = {
# 'DEFAULT_RENDERER_CLASSES': (
#     'rest_framework.renderers.JSONRenderer',
# )
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True



PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'DeClash/')
TEMPLATE_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates')
# STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = 'DeClash.S3PipelineStorage.S3PipelineStorage'
# AWS_ACCESS_KEY_ID = 'AKIAISKXNNE5RXMZBRCQ'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'elasticbeanstalk-us-west-2-603144073701'

# S3_URL = 'http://s3-us-west-2.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
# STATIC_URL = S3_URL + '/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static"),
)
TEMPLATE_DIRS = [os.path.join(PROJECT_ROOT, 'templates')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# STATIC_URL = '/static/'
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


LOGIN_REDIRECT_URL = '/'


# TEMPLATE_ROOT = os.path.join(PROJECT_ROOT, "templates")
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
# MEDIA_URL = '/media/'
# ADMIN_MEDIA_PREFIX = '/media/admin/'



# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)

# TEMPLATE_DIRS = (
#     TEMPLATE_ROOT,
#     # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
# )

# if DEBUG:
#   from local_dev_settings import *

LOGGING = {
 'version': 1,
 'disable_existing_loggers': False,
 'filters': {
 'require_debug_false': {
 '()': 'django.utils.log.RequireDebugFalse'
 }
 },
 'handlers': {
 'logfile': {
 'class': 'logging.handlers.WatchedFileHandler',
 'filename': 'D:\home\site\wwwroot\myapp.log'
 }
 },
 'loggers': {
 'django': {
 'handlers': ['logfile'],
 'level': 'ERROR',
 'propagate': False,
 }
 }
 }

