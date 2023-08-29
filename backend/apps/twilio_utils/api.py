from django.conf import settings
from twilio.rest import Client


class TwilioAPI:

    def __init__(self, settings : dict):
        self._account_sid = settings.get('account_sid', None)
        self._auth_token = settings.get('auth_token', None)
        self._from_phone_number = settings.get('from_phone_number', None)

        if not self._account_sid:
            raise Exception('account_sid not found in settings')

        if not self._auth_token:
            raise Exception('auth_token not found in settings')

    def get_twilio_client(self):
        return Client(self._account_sid, self._auth_token)

    def send_text_message(self, to_phone_number : str, message_body : str):
        """Send a text message to a phone number.

        Example response:
        {
            'MessageSid': 'SMcfb9ea88806ae7c64cc6a92dcbd4fe47',
            'DateCreated': datetime.datetime(2023, 8, 23, 2, 20, 1, tzinfo=<UTC>),
            'DateUpdated': datetime.datetime(2023, 8, 23, 2, 20, 1, tzinfo=<UTC>),
            'DateSent': None, 'To': '+18054512619',
            'From': '+18883173613',
            'MessagingServiceSid': None,
            'Body': 'HELLO WORLD!',
            'Status': 'queued'
        }
        """
        client = self.get_twilio_client()

        try:
            message = client.messages.create(
                body=message_body,
                from_=self._from_phone_number,
                to=to_phone_number
            )
            return {
                'MessageSid': message.sid,
                'DateCreated': message.date_created,
                'DateUpdated': message.date_updated,
                'DateSent': message.date_sent,
                'To': message.to,
                'From': message.from_,
                'MessagingServiceSid': message.messaging_service_sid,
                'Body': message.body,
                'Status': message.status,
            }

        except Exception as e:
            raise Exception("An error occurred:" + str(e))


def get_twilio_api():
    return TwilioAPI(settings.TWILIO_SETTINGS)
