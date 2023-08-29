from django.views.generic import ListView, DetailView
from user_conversations.models import Conversation


class ConversationListView(ListView):
    model = Conversation
    template_name = 'conversations/list.html'
    context_object_name = 'conversations'

    def get_queryset(self):
        return Conversation.objects.filter(
            target__owner=self.request.user
        ).order_by('-updated_at')

class ConversationDetailView(DetailView):
    model = Conversation
    template_name = 'conversations/detail.html'
    context_object_name = 'conversation'

    def get_queryset(self):
        return Conversation.objects.filter(
            target__owner=self.request.user
        ).order_by('-updated_at')
