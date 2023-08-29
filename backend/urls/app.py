from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = [
    #url(r'^$', RedirectView.as_view(url=reverse_lazy('account_login'))),
    #url(r'^packages/', include('deals.urls')),

    #path(r'^', include('authentication.urls')),

    #url(r'^api/', include('api.urls')),
    path(r'admin/', admin.site.urls),

    path(r'twilio/', include('twilio_utils.urls')),
    path(r'conversations/', include('user_conversations.urls')),

    # TODO: Change this to a url that makes at least one DB query.
    path(r'health/', TemplateView.as_view(template_name='health.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
