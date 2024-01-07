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
    'account_sid': os.environ['TWILIO_ACCOUNT_SID'],
    'auth_token': os.environ['TWILIO_AUTH_TOKEN'],
    'from_phone_number': os.environ['TWILIO_FROM_PHONE_NUMBER']
}

GTD_COACH = {
    'OPENAI_API_KEY': os.environ['OPENAI_API_KEY'],
    'TRELLO_API_KEY': os.environ['TRELLO_API_KEY'],
    'TRELLO_API_SECRET': os.environ['TRELLO_API_SECRET'],
    'TRELLO_API_TOKEN': os.environ['TRELLO_API_TOKEN'],
}

STORAGES['default'] = {
    'BACKEND': 'django.core.files.storage.FileSystemStorage',
}
