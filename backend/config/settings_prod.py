from .settings import *
import sys
import os
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'gtdcoach-backend.onrender.com',
]

CSRF_TRUSTED_ORIGINS = [
    'gtdcoach-backend.onrender.com',
]

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DB_URL'),
        conn_max_age=600
    )
}

COLLECTFAST_ENABLED = False

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'app-emails'


REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
)
