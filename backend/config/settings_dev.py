from .settings import *
import sys
import os


DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'host.docker.internal'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_dev.sqlite3'),
    }
}

COLLECTFAST_ENABLED = False

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'app-emails'


REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
)

TWILIO_SETTINGS = {
    'account_sid': None,
    'auth_token': None,
    'from_phone_number': None,
}


STORAGES['default'] = {
    'BACKEND': 'django.core.files.storage.FileSystemStorage',
}

GTD_COACH = {
    'OPENAI_API_KEY': None,
    'TRELLO_API_KEY': None,
    'TRELLO_API_SECRET': None,
}
