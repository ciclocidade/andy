# coding: utf-8
import os.path

DEBUG = False
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

AUTHENTICATION_BACKENDS = (
    'email_auth.EmailBackend',
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
    'pagamento',
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
LOGIN_REDIRECT_URL = '/perfil/'
LOGIN_URL = '/'

ACCOUNT_ACTIVATION_DAYS = 7

DATE_INPUT_FORMATS = ("%d/%m/%Y",)

ANUIDADE = (60.00, 120.00, 180.00)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_AGE = 3600

try:
    from local_settings import *
except ImportError:
    pass 
