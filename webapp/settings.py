"""
Would you believe this is where the magic happens? Full customization :D
"""

import os
# This bad boy makes the webapp folder the whitehouse
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Don't email this,
# SECRET_KEY = "your-secret-key-goes-here"

# I hope i remembered to turn this off
DEBUG = False
# and i did, good job me :)

ALLOWED_HOSTS = ['localhost','zenpitwebapp.herokuapp.com']


# Make a new line down there, then type that app name you just created, along with another comma

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'search',
]

# I'll let the gods at Django handle these, just skippy on by
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# We gotta handle those urls somewhere, check out urls.py of the webapp folder for our whitehouse map
ROOT_URLCONF = 'webapp.urls'

# It might be functional, but let's give it some bones
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
            'templatetags': 'templatetags.underscore_tags',

            }
        },
    },
]

WSGI_APPLICATION = 'webapp.wsgi.application'


# This webapp doesn't need this, ... yet.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Can't have one without the other

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


# Can you read this? if so, do not change
LANGUAGE_CODE = 'en-us'

# went a little nuts and changed the zone to local time from UTC
TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# all static folders be used, so join em
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# round em up, slap em in here
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
