from typing import Optional
from authentication.models import User
from authentication.fixtures import AuthenticationFixtures
from user_conversations.models import UserNumber

class UserConversationFixtures:

    def get_authentication_fixture(self):
        return AuthenticationFixtures()

    def mk_user_number(self, owner : Optional[User] = None, number : Optional[str] = None):
        """Create a user number."""
        if owner is None:
            owner = self.get_authentication_fixture().mk_user()

        if number is None:
            number = '+1234567890'

        return UserNumber.objects.create(
            owner=owner,
            number=number
        )
