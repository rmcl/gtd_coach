from .settings import *
import sys
from urllib.parse import urlparse
import os
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'gtdcoach-backend.onrender.com'
]

CSRF_TRUSTED_ORIGINS = [
    'https://gtdcoach-backend.onrender.com',
]

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DB_URL'),
        conn_max_age=600
    )
}

COLLECTFAST_ENABLED = False


STORAGES['default'] = {
    'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
}

AWS_S3_ACCESS_KEY_ID = os.environ['AWS_S3_ACCESS_KEY_ID']
AWS_S3_SECRET_ACCESS_KEY = os.environ['AWS_S3_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
)


def sentry_filter_health_transactions(event, hint):
    """Filter out healthcheck transactions from Sentry"""
    url_string = event["request"]["url"]
    parsed_url = urlparse(url_string)

    if parsed_url.path == "/health/":
        return None

    return event

sentry_sdk.init(
    dsn=os.environ['SENTRY_DSN'],
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=0.5,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    before_send_transaction=sentry_filter_health_transactions
)

ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_API_KEY']

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
