from .settings import *
import sys
import os


DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '2db4-64-52-138-16.ngrok-free.app',
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
    'account_sid': 'ACb50764e96df50eaa4419c959b72b7d4b',
    'auth_token': '0230e7ba8161d8c45cccb863a3d464f8',
    'from_phone_number': '+18883173613'
}


STORAGES['default'] = {
    'BACKEND': 'django.core.files.storage.FileSystemStorage',
}
