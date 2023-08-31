from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse

from twilio_utils.views import TwilioWebhookHandlerView
from twilio_utils.fixtures import MEDIA_MESSAGE_EX1, MEDIA_MESSAGE_EX2, MEDIA_AND_TEXT_MSG_EX3

from user_conversations.models import UserNumber
from user_conversations.fixtures import UserConversationFixtures

class TwilioWebhookHandlerViewTests(TestCase):

    @property
    def user_conversation_fixtures(self):
        return UserConversationFixtures()

    def setUp(self):
        self.factory = RequestFactory()

        un = self.user_conversation_fixtures.mk_user_number(
            number="+18054512619")
        un.save()
        self.user_number_pk = un.pk

        self.view = TwilioWebhookHandlerView.as_view()
        self.url = reverse('twilio:twilio_webhook')

    def test_media_message_ex1(self):
        request = self.factory.post(
            self.url,
            data=MEDIA_MESSAGE_EX1,
            content_type='application/x-www-form-urlencoded')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_media_message_ex2(self):
        request = self.factory.post(self.url, data=MEDIA_MESSAGE_EX2, content_type='application/x-www-form-urlencoded')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_media_and_text_msg_ex3(self):
        request = self.factory.post(self.url, data=MEDIA_AND_TEXT_MSG_EX3, content_type='application/x-www-form-urlencoded')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
