from authentication.models import User


class AuthenticationFixtures:

    def mk_user(self):
        return User.objects.create_user(
            first_name='hello',
            last_name='hello',
            email='hello@hello.com'
        )
