from user_conversations.models import Message, UserNumber
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

    def create_message_from_webhook(self, message_details : dict):
        """Create a message from a Twilio message payload."""
        message_id = message_details['MessageSid']

        try:
            return Message.objects.get(message_id=message_id)
        except Message.DoesNotExist:
            pass

        try:
            target = UserNumber.objects.get(number=message_details['From'])
        except UserNumber.DoesNotExist:
            raise Exception(f'UserNumber {message_details["From"]} not found for message')

        content = message_details['Body']

        message = Message.objects.create(
            owner=target.owner,
            target=target,
            content=content,
            message_id=message_id,
            direction='inbound',
            extra_details=message_details)

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
