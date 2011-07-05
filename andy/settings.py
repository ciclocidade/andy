# Django settings for emulta project.
import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Bruno Gola', 'brunogola@gmail.com'),
    ('Igor Garcia','abreugarcia@gmail.com'),
)

PROJECT_PATH = os.path.dirname(__file__)
HOST = 'localhost:8000'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_PATH, 'andy.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True
USE_L10N = False

MEDIA_ROOT = os.path.join(PROJECT_PATH, os.pardir, "site_media/media")
STATIC_ROOT = os.path.join(PROJECT_PATH, os.pardir, "site_media/static")
MEDIA_URL = '/site_media/media/'
STATIC_URL = '/site_media/static/'
ADMIN_MEDIA_PREFIX = '/site_media/static/admin/'

STATICFILES_DIRS = (os.path.join(PROJECT_PATH, "static"),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4qc9asdgauseyi172guygUG@8d7g2idug8e2i7gidgU@Id7g92i7gdi'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'andy.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'south',
    'registration',
    # andy apps
    'cadastro',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTH_PROFILE_MODULE = 'cadastro.Member'

ACCOUNT_ACTIVATION_DAYS = 7

DATETIME_INPUT_FORMATS = ("%m/%d/%Y %I:%M %p" , '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d',
    '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M', '%m/%d/%Y',
    '%m/%d/%y %H:%M:%S', '%m/%d/%y %H:%M', '%m/%d/%y')

EMAIL_HOST = 'localhost'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'bgola'
EMAIL_HOST_PASSWORD = 'x'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from local_settings import *
except ImportError:
    pass 
