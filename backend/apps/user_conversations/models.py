from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from authentication.models import User


class UserNumber(models.Model):
    """Phone numbers that can receive messages."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=15, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.number} - {self.owner.email} '


class Message(models.Model):
    """Messages received from Twilio."""

    direction = models.CharField(
        max_length=10,
        null=False,
        choices=(
            ('inbound', 'inbound'),
            ('outbound', 'outbound')
        ))

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.ForeignKey(
        UserNumber,
        on_delete=models.CASCADE,
        related_name='target_messages',
        null=False)

    message_id = models.CharField(max_length=255, unique=True)

    content = models.TextField(blank=True, null=True)
    extra_details = models.JSONField(encoder=DjangoJSONEncoder)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    conversation = models.ForeignKey(
        'Conversation',
        on_delete=models.CASCADE,
        related_name='messages',
        null=True)

def message_media_path(message_media_obj, filename):
    message = message_media_obj.message
    return f'media/{message.owner.pk}/{filename}'

class MessageMedia(models.Model):
    """Media attached to a message."""

    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='media')

    media_message_id = models.CharField(max_length=255, unique=True)

    file = models.FileField(
        upload_to=message_media_path)

    file_type = models.CharField(max_length=100, null=False, blank=False)
    extra_details = models.JSONField(encoder=DjangoJSONEncoder)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Conversation(models.Model):
    """A conversation with a user."""

    target = models.ForeignKey(
        UserNumber,
        on_delete=models.CASCADE,
        related_name='conversations',
        null=False)

    status = models.CharField(
        max_length=10,
        null=False,
        choices=(
            ('active', 'active'),
            ('completed', 'completed'),
            ('declined', 'declined'),
            ('aborted', 'aborted')
        ))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
