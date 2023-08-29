# from allauth.account.models import EmailAddress
# from allauth.exceptions import ImmediateHttpResponse
# from django.shortcuts import redirect
# from django.contrib import messages
from allauth.account.adapter import DefaultAccountAdapter

from organizations.models import Organization
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field

        data = form.cleaned_data
        # create organization, later attach user to organization
        organization = Organization.objects.create(name=data['business_name'],
                                                   domain=data['domain'])
        if organization:
            user.organization = organization

        # create user
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        user_email(user, email)
        if first_name:
            user_field(user, 'first_name', first_name)
        if last_name:
            user_field(user, 'last_name', last_name)
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()

        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()


        return user
