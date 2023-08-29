from django.urls import include, path
from .views import (
    ConversationListView,
    ConversationDetailView,
)

app_name = 'conversations'

urlpatterns = [
    path('', ConversationListView.as_view(), name='list'),
    path('<int:pk>/', ConversationDetailView.as_view(), name='detail'),
]
