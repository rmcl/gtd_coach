import os.path
from mimetypes import guess_extension
from django.core.files.temp import NamedTemporaryFile
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

from twilio_utils.api import get_twilio_api
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

    def handle_twilio_message(self, webhook_payload):
        service = get_user_conversation_service()

        new_message = service.create_message_from_webhook(webhook_payload)

        num_media = int(webhook_payload.get('NumMedia', 0))
        if num_media > 0:
            retrieved_media = self.process_media_message(
                new_message,
                webhook_payload)

        # Todo figure this out
        #service.find_and_update_conversation(new_message)

    def save_media_from_url_to_field(self, content_type, media_url, file_field):
        """Save media from a url to a file field."""
        twilio_api = get_twilio_api()
        media_content = twilio_api.get_media_from_url(media_url)

        extension = guess_extension(content_type)
        base_media_name = f'{os.path.basename(media_url)}{extension}'

        with NamedTemporaryFile(delete=True) as temp_file:
            temp_file.write(media_content)
            temp_file.flush()
            file_field.save(base_media_name, temp_file, save=True)

    def process_media_message(self, message, webhook_message):
        """Process a media message and return the media."""
        service = get_user_conversation_service()

        retrieved_media = []
        num_media = int(webhook_message.get('NumMedia', 0))
        for i in range(num_media):
            media_url = webhook_message.get(f'MediaUrl{i}', None)
            media_content_type = webhook_message.get(f'MediaContentType{i}', None)
            message_media = service.create_media_from_webhook(
                message,
                media_content_type=media_content_type,
                raw_message=webhook_message)

            self.save_media_from_url_to_field(media_content_type, media_url, message_media.file)

            retrieved_media.append(message_media)

        return retrieved_media

    def post(self, request, *args, **kwargs):
        # Get the message the user sent our Twilio number

        self.handle_twilio_message(self.request.POST)

        # Start our TwiML response. We want to send a blank TwiML message back.
        resp = MessagingResponse()
        return HttpResponse(
            str(resp),
            status=200,
            content_type='application/xml')
