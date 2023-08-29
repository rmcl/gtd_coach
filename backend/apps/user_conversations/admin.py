from django.contrib import admin
from user_conversations.models import Message, UserNumber, Conversation

@admin.register(UserNumber)
class UserNumbers(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'number',
        'created_at',
        'updated_at'
    )

@admin.register(Message)
class Messages(admin.ModelAdmin):
    list_display = (
        'id',
        'message_id',
        'target',
        'direction',
        'content',
        'owner',
        'created_at',
        'updated_at'
    )


class ConversationMessageInline(admin.TabularInline):
    model = Message
    extra = 0

@admin.register(Conversation)
class Conversations(admin.ModelAdmin):
    list_display = (
        'id',
        'target',
        'status'
    )

    inlines = [
        ConversationMessageInline
    ]
