from django.urls import include, path
from .views import (
    TwilioWebhookHandlerView
)

app_name = 'twilio'

urlpatterns = [
    path('webhook', TwilioWebhookHandlerView.as_view(), name='twilio_webhook'),
]
