
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

from user_conversations.service import get_user_conversation_service

@method_decorator(csrf_exempt, name='dispatch')
class TwilioWebhookHandlerView(View):
    """Handle incoming Twilio webhook."""

    TWILIO_FIELDS = [
        'ToCountry',
        'ToState',
        'SmsMessageSid',
        'ToCity',
        'FromZip',
        'SmsSid',
        'FromState',
        'SmsStatus',
        'FromCity',
        'Body',
        'FromCountry',
        'To',
        'MessagingServiceSid',
        'ToZip',
        'NumSegments',
        'MessageSid',
        'AccountSid',
        'From',
        'ApiVersion',
        'NumMedia',
        'MediaContentType0',
    ]

    def handle_twilio_message(self, message):
        print('Message received: {}'.format(message))

        service = get_user_conversation_service()
        new_message = service.create_message_from_webhook(message)

        # Todo figure this out
        #service.find_and_update_conversation(new_message)

    def get_twilio_message_data(self, post_data):
        return {
            field: post_data.get(field, None)
            for field in self.TWILIO_FIELDS
        }

    def post(self, request, *args, **kwargs):
        # Get the message the user sent our Twilio number
        message = self.get_twilio_message_data(self.request.POST)
        self.handle_twilio_message(message)

        # Start our TwiML response. We want to send a blank TwiML message back.
        resp = MessagingResponse()
        return HttpResponse(
            str(resp),
            status=200,
            content_type='application/xml')
