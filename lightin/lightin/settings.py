"""
Django settings for lightin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if 'MYSQL_USER' in os.environ:
    MYSQL_USER = os.environ['MYSQL_USER']
    MYSQL_PASS = os.environ['MYSQL_PASS']
    MYSQL_HOST = os.environ['MYSQL_HOST']
    MYSQL_PORT = os.environ['MYSQL_PORT']
    MYSQL_NAME = os.environ['MYSQL_NAME']
else:
    MYSQL_USER = ''
    MYSQL_PASS = ''
    MYSQL_HOST = ''
    MYSQL_PORT = '3306'
    MYSQL_NAME = 'lightin'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lzc8+jyh=6)*94&))xsq3av!_hm$x+1_j)2kmxqe@(zeuzp613'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mobiconf',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lightin.urls'

WSGI_APPLICATION = 'lightin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : MYSQL_NAME,
        'USER'     : MYSQL_USER,
        'HOST'     : MYSQL_HOST,
        'PORT'     : MYSQL_PORT,
        'PASSWORD' : MYSQL_PASS,
        
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    'mobiconf/static',
)
