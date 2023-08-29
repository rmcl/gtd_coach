import operator
import re
import pytz

from django.utils import timezone
from django.conf import settings
from django.utils.cache import patch_vary_headers

from subdomains.utils import get_domain

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    # Pre Django 1.10 middleware does not require the mixin.
    MiddlewareMixin = object

lower = operator.methodcaller('lower')

UNSET = object()

"""
Django 1.10 broke how middleware works.

http://stackoverflow.com/questions/38897320/typeerror-object-has-no-parameters-using-django-subdomains
https://github.com/tkaemming/django-subdomains/pull/60/commits/63405c239148308bf214f950c0cff50d7f29b23d

Note: set up site in django admin before using subdomains
"""

class SubdomainMiddleware(MiddlewareMixin):
    """
    A middleware class that adds a ``subdomain`` attribute to the current request.
    """
    def get_domain_for_request(self, request):
        """
        Returns the domain that will be used to identify the subdomain part
        for this request.
        """
        return get_domain()

    def process_request(self, request):
        """
        Adds a ``subdomain`` attribute to the ``request`` parameter.
        """
        domain, host = map(lower,
            (self.get_domain_for_request(request), request.get_host()))

        pattern = r'^(?:(?P<subdomain>.*?)\.)?%s(?::.*)?$' % re.escape(domain)
        matches = re.match(pattern, host)

        if matches:
            request.subdomain = matches.group('subdomain')
        else:
            request.subdomain = None


class SubdomainURLRoutingMiddlewareFix(SubdomainMiddleware):
    """
    A middleware class that allows for subdomain-based URL routing.
    """
    def process_request(self, request):
        """
        Sets the current request's ``urlconf`` attribute to the urlconf
        associated with the subdomain, if it is listed in
        ``settings.SUBDOMAIN_URLCONFS``.
        """
        super(SubdomainURLRoutingMiddlewareFix, self).process_request(request)

        subdomain = getattr(request, 'subdomain', UNSET)

        request.urlconf = settings.ROOT_URLCONF
        if subdomain is not UNSET:
            urlconf = settings.SUBDOMAIN_URLCONFS.get(subdomain)
            if urlconf is not None:
                request.urlconf = urlconf

    def process_response(self, request, response):
        """
        Forces the HTTP ``Vary`` header onto requests to avoid having responses
        cached across subdomains.
        """
        if getattr(settings, 'FORCE_VARY_ON_HOST', True):
            patch_vary_headers(response, ('Host',))

        return response


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tzname = request.session.get('django_timezone', 'US/Pacific')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
