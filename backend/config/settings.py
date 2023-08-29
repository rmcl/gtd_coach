"""
Django settings for getthedocs project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import sys
import os
import locale

# set locale
locale.setlocale(locale.LC_ALL, '')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r-jkxhx@00f#gvpyqdx(d%(dddzyxm^2n&!=*@i*u_()58w@zqm98'

SESSION_COOKIE_NAME = "gtdcoach.io"

COLLECTFAST_ENABLED = True # set to False on local dev

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    #'collectfast',
    'django.contrib.staticfiles',
    'subdomains',
    'storages',
    #'django_markup',
    'rest_framework',
    'rest_framework.authtoken',
    #'django_filters',
    #'django_gravatar',
    #'djangobower',
    #'crispy_forms',
    #'etc',
    #'colorfield',

    'health_check',
    'authentication',
    'user_conversations',


    #'phonenumber_field',
    #'bootstrapform',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

]

BOWER_INSTALLED_APPS = [
    'bootstrap#3.3.7',
    'enyo/dropzone#v4.3.0',
    'font-awesome#4.7.0',
    'bootstrap-toggle#2.2.2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'utils.middleware.SubdomainURLRoutingMiddlewareFix',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.middleware.TimezoneMiddleware',
    'authentication.middleware.password_change_redirect.PasswordChangeRedirectMiddleware',
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

SITE_ID = 1

ROOT_URLCONF = 'urls.app'

# A dictionary of urlconf module paths, keyed by their subdomain.
SUBDOMAIN_URLCONFS = {
    None: 'urls.app',  # no subdomain, e.g. ``example.com``
    'app': 'urls.app',
}

BOWER_COMPONENTS_ROOT = BASE_DIR + '/frontend/lib'
CRISPY_TEMPLATE_PACK = 'bootstrap3'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    )
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates/allauth/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static'
            ],
        },
    },
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend/build'),
)

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
        },
    }
}


AUTH_USER_MODEL = 'authentication.User'
LOGIN_URL = '/accounts/login/'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '%s/static' % (BASE_DIR)

MEDIA_ROOT = '%s/media/' % (BASE_DIR)
MEDIA_URL = '/media/'

# Start allauth settings
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = '/deals/'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_SIGNUP_FORM_CLASS = 'authentication.forms.CustomSignupForm'
ACCOUNT_LOGOUT_ON_GET = True  # don't ask on sign out
# SOCIALACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
# SOCIALACCOUNT_EMAIL_REQUIRED = False
# SOCIALACCOUNT_ADAPTER = 'authentication.account_adapter.CustomSocialAccountAdapter'
ACCOUNT_ADAPTER = 'authentication.account_adapter.CustomAccountAdapter'
ACCOUNT_USERNAME_BLACKLIST = [
    'admin',
    'root'
]
ACCOUNT_USERNAME_VALIDATORS = None
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# email
NOREPLY_EMAIL = 'hello@docgather.com'
DEFAULT_FROM_EMAIL = 'support@docgather.com'
EMAIL_COMPANY_NAME = 'DocGather'
EMAIL_COMPANY_URL = 'https://www.docgather.com'


ENABLE_GOOGLE_TAG_MANAGER = False

TEMPLATE_ACCESSIBLE_SETTING_VARS = [
    'DEBUG',
    'ENABLE_GOOGLE_TAG_MANAGER'
]
