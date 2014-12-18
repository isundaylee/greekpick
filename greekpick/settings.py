# -*- coding: utf-8 -*-

"""
Django settings for greekpick project.

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
SECRET_KEY = 'xneact$ywtln%(w2+$c10ac&%@cv--h)87+h8s1logb3cwr%l+'

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
    'foundation',
    'poll',
    'jquery',
    'django_ajax',
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

ROOT_URLCONF = 'greekpick.urls'

WSGI_APPLICATION = 'greekpick.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static"),
)

# Template directories
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

# The lovely letters :)
LETTER_LIST = [
  ('alpha', ('Α', 'α')),
  ('beta', ('Β', 'β')),
  ('gamma', ('Γ', 'γ')),
  ('delta', ('Δ', 'δ')),
  ('epsilon', ('Ε', 'ε')),
  ('zeta', ('Ζ', 'ζ')),
  ('eta', ('Η', 'η')),
  ('theta', ('Θ', 'θ')),
  ('iota', ('Ι', 'ι')),
  ('kappa', ('Κ', 'κ')),
  ('lambda', ('Λ', 'λ')),
  ('mu', ('Μ', 'μ')),
  ('nu', ('Ν', 'ν')),
  ('xi', ('Ξ', 'ξ')),
  ('omicon', ('Ο', 'ο')),
  ('pi', ('Π', 'π')),
  ('rho', ('Ρ', 'ρ')),
  ('sigma', ('Σ', 'σ')),
  ('tau', ('Τ', 'τ')),
  ('upsilon', ('Υ', 'υ')),
  ('phi', ('Φ', 'φ')),
  ('chi', ('Χ', 'χ')),
  ('psi', ('Ψ', 'ψ')),
  ('omega', ('Ω', 'ω'))
]
