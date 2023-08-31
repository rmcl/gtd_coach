from user_conversations.models import Message, UserNumber, MessageMedia
from twilio_utils.api import get_twilio_api


class UserConversationService:
    """Service for handling user conversations."""

    def send_message(self, target : UserNumber, content : str):
        """Send a message to a user."""
        twilio_api = get_twilio_api()
        message_details = twilio_api.send_text_message(target.number, content)

        message = Message.objects.create(
            owner=target.owner,
            target=target,
            content=content,
            message_id=message_details['MessageSid'],
            direction='outbound',
            extra_details=message_details)

        return message

    def create_media_from_webhook(
        self,
        message : Message,
        message_sid : str,
        media_content_type : str,
        raw_message : dict
    ):
        """Create a media from a Twilio message payload."""
        message_media = MessageMedia.objects.create(
            message=message,
            media_message_id=message_sid,
            file_type=media_content_type,
            extra_details=raw_message)

        return message_media


    def create_message_from_webhook(self, webhook_payload : dict):
        """Create a message from a Twilio message payload."""
        message_id = webhook_payload['MessageSid']

        try:
            return Message.objects.get(message_id=message_id)
        except Message.DoesNotExist:
            pass

        try:
            target = UserNumber.objects.get(number=webhook_payload['From'])
        except UserNumber.DoesNotExist:
            raise Exception(f'UserNumber {webhook_payload["From"]} not found for message')

        content = webhook_payload['Body']

        message = Message.objects.create(
            owner=target.owner,
            target=target,
            content=content,
            message_id=message_id,
            direction='inbound',
            extra_details=webhook_payload)

        return message

    def find_and_update_conversation(self, message):
        """Find and update the conversation for a message."""
        conversations = message.conversation.filter(
            status='active'
        )

        conversation = conversations.first()

        if conversation:
            message.conversation = conversation
            message.save()

def get_user_conversation_service():
    return UserConversationService()
