from django import forms
import django.contrib.auth.forms as auth_forms
from django.contrib.auth import get_user_model
import authentication.models as auth_models

User = get_user_model()


class UserCreationForm(auth_forms.UserCreationForm):
    """A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(UserCreationForm, self).__init__(*args, **kargs)

    class Meta(auth_forms.UserCreationForm.Meta):
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )


class UserChangeForm(auth_forms.UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)

    class Meta(auth_forms.UserChangeForm.Meta):
        model = User


# custom user registration form
class CustomSignupForm(forms.Form):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super(CustomSignupForm, self).clean()
        return

    def signup(self, request, user):
        pass
