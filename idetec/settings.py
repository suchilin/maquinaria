"""
Django settings for idetec project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@yhq4e@p36^u*@zama8n-4heu*%dd1zzq+%hn9&lh9y+&mb0b3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'widget_tweaks',
    'solicitudes',
    'registration',
    'dbupdater',
    'mathfilters',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'idetec.urls'

WSGI_APPLICATION = 'idetec.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'idetec.db3'),
    }

    # 'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': 'idetec',                      # Or path to database file if using sqlite3.
        # # The following settings are not used with sqlite3:
        # 'USER': 'proagro',
        # 'PASSWORD': 'Proagro_2014',
        # 'HOST': '10.102.4.4',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        # 'PORT': '',                      # Set to empty string for default.
    # }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/idetec/'

#TEMPLATE_CONTEXT_PROCESSORS = (
    #"django.core.context_processors.request",
#)

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

GRAPPELLI_ADMIN_TITLE = "IDETEC"


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

ACCOUNT_ACTIVATION_DAYS = 7

LOGIN_REDIRECT_URL = '/solicitudes15/'

LOGIN_URL = '/idetec/accounts/login'

TEMPLATE_DIRS = (
            os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/'),
            )
USE_THOUSAND_SEPARATOR = True
