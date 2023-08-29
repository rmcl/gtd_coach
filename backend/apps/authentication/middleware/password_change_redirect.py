import re
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponseRedirect
from django.contrib import messages


class PasswordChangeRedirectMiddleware(object):
    """ Checks in request if user is authenticated and
        if password_change_required flag in User instance
        is set to True. If True - redirect to password_change
        page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        if request.user.password_change_required:
            allowed_urls = [
                reverse(
                    'account_login',
                    urlconf=request.urlconf
                ),
                reverse(
                    'account_logout',
                    urlconf=request.urlconf
                ),
                reverse(
                    'account_change_password',
                    urlconf=request.urlconf
                )
            ]

            for url in allowed_urls:
                if re.search(r"^%s.*" % url, request.path, re.IGNORECASE):
                    response = self.get_response(request)
                    return response

            messages.add_message(
                request,
                messages.INFO,
                'A password change is required. Please select a new password.'
            )

            return HttpResponseRedirect(
                reverse(
                    'account_change_password',
                    urlconf=request.urlconf
                )
            )

        return self.get_response(request)
