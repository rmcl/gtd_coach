from django.urls import include, path
from authentication.views import PasswordChangeView
from authentication import views

urlpatterns = [
    path(
        r'accounts/password/change/',
        PasswordChangeView.as_view(),
        name='account_change_password'
    ),
    path(r'accounts/', include('allauth.urls')),
]
