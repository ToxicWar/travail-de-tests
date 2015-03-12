# coding: utf-8
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'topsecret'

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

    'testtask',

    'django_nose',
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

ROOT_URLCONF = 'site_testtask.urls'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

# Internationalization

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

MODELS_FILE = os.path.join(BASE_DIR, 'models.yaml')

# Other settings

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
coverage_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'report')

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=testtask',
    '--cover-html',
    '--cover-html-dir=%s' % coverage_dir,
    '--cover-inclusive',
    '--cover-erase',
    # '--rednose',
    '-x',
]
